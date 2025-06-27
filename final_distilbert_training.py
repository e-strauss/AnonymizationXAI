import json
from pathlib import Path
import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from tqdm import tqdm

# === Step 1: Load data from JSONL files ===
def load_jsonl(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            data.append(item)
    return [x["text"] for x in data], [x["label"] for x in data]

train_texts, train_labels = load_jsonl("train.jsonl")
val_texts, val_labels = load_jsonl("val.jsonl")
test_texts, test_labels = load_jsonl("test.jsonl")

print((f"Loaded {len(train_texts)} training samples, "
       f"{len(val_texts)} validation samples, "
       f"{len(test_texts)} test samples."))

# === Step 2: Encode labels ===
label_encoder = LabelEncoder()
train_labels = label_encoder.fit_transform(train_labels)
val_labels = label_encoder.transform(val_labels)
test_labels = label_encoder.transform(test_labels)
num_labels = len(label_encoder.classes_)

# === Step 3: Tokenizer ===
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

# === Step 4: Custom Dataset ===
class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=512):
        self.encodings = tokenizer(texts, truncation=True, padding=True, max_length=max_len)
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

# === Step 5: Create Datasets and DataLoaders ===
train_dataset = TextDataset(train_texts, train_labels, tokenizer)
val_dataset = TextDataset(val_texts, val_labels, tokenizer)
test_dataset = TextDataset(test_texts, test_labels, tokenizer)

train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=16)
test_loader = DataLoader(test_dataset, batch_size=16)

lengths = [len(tokenizer.encode(t)) for t in train_texts]
print(f"Max input length: {max(lengths)}")
print(f"Percentage over 512: {sum(l > 512 for l in lengths) / len(lengths) * 100:.2f}%")


# === Step 6: Model, Optimizer, Device ===
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=num_labels)
model.to(device)
optimizer = AdamW(model.parameters(), lr=2e-5)

# === Step 7: Training + Evaluation Loops ===
def train(model, loader):
    model.train()
    total_loss = 0
    for batch in tqdm(loader, desc="Training"):
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        total_loss += loss.item()
    return total_loss / len(loader)

def evaluate(model, loader):
    model.eval()
    preds, true = [], []
    with torch.no_grad():
        for batch in tqdm(loader, desc="Evaluating"):
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            logits = outputs.logits
            preds.extend(torch.argmax(logits, axis=1).cpu().numpy())
            true.extend(batch['labels'].cpu().numpy())
    return preds, true

# === Step 8: Train the model ===
for epoch in range(1):
    print(f"\nEpoch {epoch+1}")
    train_loss = train(model, train_loader)
    print(f"Train Loss: {train_loss:.4f}")
    
    val_preds, val_true = evaluate(model, val_loader)
    print(classification_report(val_true, val_preds, target_names=[str(x) for x in label_encoder.classes_]))
# === Step 9: Final test evaluation ===
print("\n=== Test Evaluation ===")
test_preds, test_true = evaluate(model, test_loader)
print(classification_report(test_true, test_preds, target_names=[str(x) for x in label_encoder.classes_]))
print(f"Predictions: {len(test_preds)}, Ground Truth: {len(test_true)}")

# === Step 10: Save model & tokenizer ===
model.save_pretrained("final_distilbert-model")
tokenizer.save_pretrained("final_distilbert-model")
