import json

def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            candidates.append(json.loads(line))

    return candidates

