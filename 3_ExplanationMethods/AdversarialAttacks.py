import json
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from textattack.models.wrappers import HuggingFaceModelWrapper
from textattack.attack_recipes import PWWSRen2019, BAEGarg2019, TextFoolerJin2019, BERTAttackLi2020
from textattack import Attacker, AttackArgs
from textattack.datasets import Dataset
import random
import torch 

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#Load model and tokenizer
model_path = model_path = "../DB-bio/final_distilbert-model"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.to(device)  

tokenizer = AutoTokenizer.from_pretrained(model_path)
wrapped_model = HuggingFaceModelWrapper(model, tokenizer)

#Load dataset 
jsonl_path = "/Users/yoana/Desktop/Quality and Usability Project/DB-bio/combined_val_and_val_sft_anonymized.jsonl"
examples = []
with open(jsonl_path, "r") as f:
    for line in f:
        obj = json.loads(line)
        examples.append((obj["text"], int(obj["label"])))  
random.shuffle(examples) 

dataset = Dataset(examples[:50])  

#Build attack recipe
attack = BERTAttackLi2020.build(wrapped_model)
attack.transformation.max_candidates = 15


#Configure attack 
attack_args = AttackArgs(
    num_examples=50,
    disable_stdout=False,
    log_to_txt="/Users/yoana/Desktop/Quality and Usability Project/DB-bio/TextAttack final results/bert_bertattack_log.txt"
)

#Run the attack
attacker = Attacker(attack, dataset, attack_args)
attacker.attack_dataset()
