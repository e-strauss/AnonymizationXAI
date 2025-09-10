import re
import csv

with open("bert_bertattack_log.txt", "r", encoding="utf-8") as file:
    content = file.read()

blocks = content.strip().split("--------------------------------------------- Result ")

rows = []

for block in blocks:
    if not block.strip():
        continue

    if '[[[FAILED]]]' in block:
        continue

    match = re.match(r"(\d+)", block.strip())
    attack_index = match.group(1) if match else "?"

    try:
        parts = block.split("\n\n", 1)
        original_text = parts[1].split("\n\n")[0].strip()
    except IndexError:
        continue

    bracketed_words = re.findall(r"\[\[([^\[\]]+)\]\]", original_text)
    clean_words = [w.strip() for w in bracketed_words if w.strip()]
    formatted_words = "[" + ", ".join(clean_words) + "]"

    clean_text = re.sub(r"\[\[([^\[\]]+)\]\]", r"\1", original_text)

    rows.append([attack_index, formatted_words, clean_text])

with open("bracketed_words_with_clean_text.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Attack Index", "Bracketed Words", "Original Text (Cleaned)"])
    writer.writerows(rows)

