from datasets import load_dataset
import json
from sklearn.model_selection import train_test_split


def load_jsonl(path):
    with open(path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')


def stratified_70_20_10_split(data, label_key, seed=42):
    labels = [item[label_key] for item in data]

    # Step 1: Split off 10% test
    rest_data, test_data, rest_labels, _ = train_test_split(
        data, labels, test_size=0.1, stratify=labels, random_state=seed
    )

    # Step 2: Split remaining 90% into 70% train and 20% val (70/90 ≈ 0.777...)
    train_data, val_data, _, _ = train_test_split(
        rest_data, rest_labels, test_size=2 / 9, stratify=rest_labels, random_state=seed
    )

    return train_data, val_data, test_data



jsonl_path = '../DB-bio/training_data.jsonl'
label_key = 'label'

data = load_jsonl(jsonl_path)
train, val, test = stratified_70_20_10_split(data, label_key)

save_jsonl(train, '../DB-bio/train.jsonl')
save_jsonl(val, '../DB-bio/val.jsonl')
save_jsonl(test, '../DB-bio/test.jsonl')
