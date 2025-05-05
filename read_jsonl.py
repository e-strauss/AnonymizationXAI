import json, pandas as pd


def read_jsonl(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    lines_parsed = [json.loads(line) for line in lines]
    column_names = [c for c in lines_parsed[0].keys()]

    # Assert same schema
    for line in lines_parsed:
        for col in column_names:
            assert col in line.keys()
        for col in line.keys():
            assert col in column_names

    column_data = [[] for _ in column_names]
    for line in lines_parsed:
        for i, col in enumerate(column_names):
            column_data[i].append(line[col])

    df = pd.DataFrame(list(zip(*column_data)), columns=column_names)

    return df
