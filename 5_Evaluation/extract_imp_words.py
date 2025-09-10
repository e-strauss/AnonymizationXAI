import re

def remove_double_brackets_keep_content(text):
    return re.sub(r"\[\[|\]\]", "", text)
with open("/content/bert_textfooler_log.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

collecting = False
line_counter = 0
results = []
text1, text2 = "", ""
collecting_text = False

for line in lines:
    if "--> [[[FAILED]]]" in line:
        continue  # skip failed examples
    elif "-->" in line:
        collecting_text = True
        current_result = {"meta": line.strip(), "text1": "", "text2": ""}
        continue
    elif collecting_text and not current_result["text1"]:
        current_result["text1"] = line.strip()
    elif collecting_text and not current_result["text2"]:
        current_result["text2"] = line.strip()
        results.append(current_result)
        collecting_text = False  # done collecting this example


print(text1)