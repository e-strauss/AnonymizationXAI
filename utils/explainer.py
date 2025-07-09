import time
import requests
import torch
from captum.attr import LayerIntegratedGradients
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer

function_words = ["a", "an", "is", "from", "in", "and", "the", "were", "was", "of", "to", "at", "by", "for", 'on',
                  "also", "as", 'with']


def merge_word_pieces(tokens, scores, tids):
    merged_tokens = []
    merged_scores = []
    merged_ids = []
    current_token, current_score, current_ids = "", 0.0, []

    for token, score, tid in zip(tokens, scores, tids):
        if token.startswith("##"):
            current_token += token[2:]
            current_score += abs(score)
            current_ids.append(int(tid))
        else:
            if current_token:
                merged_tokens.append(current_token)
                merged_scores.append(current_score)
                merged_ids.append(tuple(current_ids) if len(current_ids) > 1 else current_ids[0])
            current_token = token
            current_score = abs(score)
            current_ids = [int(tid)]

    if current_token:
        merged_tokens.append(current_token)
        merged_scores.append(current_score)
        merged_ids.append(tuple(current_ids))
    return merged_tokens, merged_scores, merged_ids


class FeatureImportanceGradient:
    def __init__(self, force_cpu=False, max_length=512, merge_tokens=True, filter_function_words=True):
        startup_start_time = time.time()

        self.filter = {"[CLS]", "[SEP]", "[PAD]", '—', '–', '-', '.', ',', '"', ':', "(", ")", "\\"}
        if filter_function_words:
            self.filter.update(function_words)

        self.merge_tokens = merge_tokens
        self.max_length = max_length
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = DistilBertForSequenceClassification.from_pretrained("../final_distilbert-model/")
        self.model.eval()

        # Detect MPS (Apple Silicon GPU)
        self.device = torch.device("mps" if torch.backends.mps.is_available() and not force_cpu else "cpu")
        print(f"Using device: {self.device}")
        self.model.to(self.device)
        startup_end_time = time.time()

        def forward(_input_ids, _attention_mask):
            return self.model(input_ids=_input_ids, attention_mask=_attention_mask).logits

        self.lig = LayerIntegratedGradients(forward, self.model.distilbert.embeddings)
        print(f"Startup time: {startup_end_time - startup_start_time}")

    def compute_attributions(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding='max_length',
                                max_length=self.max_length)
        inputs.to(self.device)
        input_ids = inputs['input_ids']
        input_ids.to(self.device)
        attention_mask = inputs['attention_mask']
        attention_mask.to(self.device)
        baseline = torch.zeros_like(input_ids)
        baseline.to(self.device)

        with torch.no_grad():
            logits = self.model(input_ids, attention_mask=attention_mask).logits
            target = torch.argmax(logits, dim=1).item()
            conf = torch.softmax(logits, dim=1)[0][target].item()

        attributions, delta = self.lig.attribute(
            inputs=input_ids,
            baselines=baseline,
            additional_forward_args=attention_mask,
            target=target,
            return_convergence_delta=True
        )
        return input_ids, target, conf, attributions, delta

    def select_top_k_important_from_attribution(self, attributions, input_ids, k=5, merge_tokens=True,
                                                return_ids=False, return_scores=False, verbose=False):
        tokens = self.tokenizer.convert_ids_to_tokens(input_ids)
        scores = torch.linalg.norm(attributions, dim=-1, ).squeeze(0).tolist()

        if merge_tokens:
            tokens, attributions, input_ids = merge_word_pieces(tokens, scores, input_ids)

        unique_tokens = {}
        for t, s, tid in zip(tokens, scores, input_ids):
            if t not in self.filter:
                _, old_score = unique_tokens.get(tid, (None, 0))
                unique_tokens[tid] = (t, max(old_score, s))

        if verbose:
            print("Unique tokens: ", unique_tokens)

        if return_ids and return_scores:
            triples = [(key, value[0], value[1]) for key, value in unique_tokens.items()]
            return sorted(triples, key=lambda x: x[2], reverse=True)[:k]
        else:
            top_k = sorted(unique_tokens.values(), key=lambda x: [1])[:k]
            if return_scores:
                return top_k
            return [word for (word, score) in top_k]

    def get_feature_importance(self, text, return_ids=False, return_scores=False, return_target=False, k=15):
        input_ids, target, conf, attributions, delta = self.compute_attributions(text)
        words = self.select_top_k_important_from_attribution(attributions, input_ids[0], merge_tokens=self.merge_tokens,
                                                             return_scores=return_scores, return_ids=return_ids, k=k)

        if return_target:
            return target, words
        return words


def mark_important_tokens(text, important_tokens):
    marked_text = text.replace("[", "").replace("]", "").lower()
    for token in important_tokens:
        marked_text = marked_text.replace(" {} ".format(token), " [{}] ".format(token))
    return marked_text


class NaturalLanguageExplainer:
    def __init__(self, model="gpt-3.5-turbo", api="https://api.openai.com/v1/chat/completions", max_length=512):
        self.model = model
        self.api = api
        self.OPENAI_API_KEY = "EMPTY"
        with open("../.openai_key.txt") as f:
            self.OPENAI_API_KEY = f.read().strip()

        self.feature_importance = FeatureImportanceGradient(max_length=max_length)
        self.max_length = max_length

    def _send_request(self, messages):
        headers = {
            "Authorization": f"Bearer {self.OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.0
        }

        response = requests.post(self.api, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        return reply

    def get_explanation(self, text, verbose=False):
        target, important_tokens = self.feature_importance.get_feature_importance(text, return_target=True)
        marked_text = mark_important_tokens(text.lower(), important_tokens)

        if verbose:
            print(marked_text)

        prompt = (("Explain why the following text is classified as {}anonymized. Words in square brackets [] are "
                  "important words for the classification of this text. This is the text: ")
                  .format("not " if target == 0 else ""))
        messages = [{"role": "user", "content": prompt + marked_text}]
        explanation = self._send_request(messages)
        return explanation


if __name__ == '__main__':
    ttext = ('Stephen J. Gordon (born 4 September 1986) is a chess grandmaster from Oldham, Greater Manchester, '
             'England. In September 2004 he took a break from his A-level studies at The Blue Coat School, Oldham '
             'to compete in the thirteenth Monarch Assurance Isle of Man International. In 2005, while still a FIDE '
             'Master, he finished 6th in the British Championships ahead of a Grandmaster and several International '
             'Masters. At the EU Individual Open Chess Championship held at Liverpool in 2006, he led the tournament '
             'after eight rounds and finished a very creditable (joint) second, a half point behind winner Nigel Short '
             'and level with Luke McShane among others. Probably his best result to date however, was second place in '
             'the 2007 British Championship, narrowly losing his share of the lead in the final round. In previous '
             'rounds, he defeated both tournament victor Jacob Aagaard and previous champion Jonathan Rowson. By 2008, '
             'his rating had reached grandmaster level, although the title itself had not yet been secured. At the '
             'British Championship in Liverpool, he almost repeated his performance of the previous year, by taking a '
             'share of third place. He was the British under-21 Champion each consecutive year between 2005 and 2008. '
             'He became a grandmaster on 1 August 2009. He has been one of the co-presenters of the chess podcast The '
             'Full English Breakfast since its inaugural show in October 2010.')
    explainer = NaturalLanguageExplainer(max_length=256)
    print(explainer.get_explanation(ttext, verbose=True))
