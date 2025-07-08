import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from captum.attr import LayerIntegratedGradients


class DistilBertAttributor:
    def __init__(self, model_path: str, force_cpu: bool = False, max_length: int = 128):
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)
        self.model.eval()

        if not force_cpu and torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif not force_cpu and torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        print("Using {} device".format(self.device))
        self.model.to(self.device)

        self.max_length = max_length
        self.lig = LayerIntegratedGradients(self._forward_captum, self.model.distilbert.embeddings)

    def _forward_captum(self, input_ids, attention_mask):
        return self.model(input_ids=input_ids, attention_mask=attention_mask).logits

    def compute_attributions(self, text: str, merge_scores: bool = True, p=2):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding='max_length',
                                max_length=self.max_length)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        baseline = torch.zeros_like(input_ids).to(self.device)

        with torch.no_grad():
            logits = self.model(**inputs).logits
            target = torch.argmax(logits, dim=1).item()

        attributions, delta = self.lig.attribute(
            inputs=input_ids,
            baselines=baseline,
            additional_forward_args=attention_mask,
            target=target,
            return_convergence_delta=True
        )

        scores = attributions.norm(p=p, dim=-1).squeeze(0)
        tokens = self.tokenizer.convert_ids_to_tokens(input_ids[0])

        filter_set = {"[CLS]", "[SEP]", "[PAD]", '.', ',', "(", ")"}
        token_scores = {} if merge_scores else \
            {token: score for token, score in zip(tokens, scores)
             if token not in filter_set}

        if merge_scores:
            for token, score in zip(tokens, scores):
                if token not in filter_set:
                    if token in token_scores:
                        token_scores[token] += score
                    else:
                        token_scores[token] = score

        return target, sorted(token_scores.items(), key=lambda x: x[1], reverse=True)
