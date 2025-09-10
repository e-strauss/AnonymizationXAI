import json
import pandas as pd

file_path = "../DB-bio/train_sft.jsonl"
output_file_path = "../DB-bio/training_data.jsonl"
# Load all lines from the JSONL file
with open(file_path, "r") as file:
    data = [json.loads(line) for line in file]

mid = len(data) // 2

first_half = [{"text": entry["output"], "label": 1} for entry in data[:mid] if "output" in entry]
second_half = [{"text": entry["input"], "label": 0} for entry in data[mid:] if "input" in entry]

combined = first_half + second_half

with open(output_file_path, "w") as out_file:
    for entry in combined:
        out_file.write(json.dumps(entry) + "\n")

