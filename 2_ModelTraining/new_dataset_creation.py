import json
import pandas as pd

# Path to your file
file_path = "../DB-bio/train_sft.jsonl"
output_file_path = "../DB-bio/training_data.jsonl"
# Load all lines from the JSONL file
with open(file_path, "r") as file:
    data = [json.loads(line) for line in file]

# Compute the midpoint
mid = len(data) // 2

# First half: take "output" and label 1
first_half = [{"text": entry["output"], "label": 1} for entry in data[:mid] if "output" in entry]

# Second half: take "input" and label 0
second_half = [{"text": entry["input"], "label": 0} for entry in data[mid:] if "input" in entry]

# Combine the two halves
combined = first_half + second_half

with open(output_file_path, "w") as out_file:
    for entry in combined:
        out_file.write(json.dumps(entry) + "\n")

