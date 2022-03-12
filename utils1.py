import json

def get_candidate():
    file = open("candidates.json", "r", encoding="utf - 8")
    data = json.load(file)
    file.close()
    return data


