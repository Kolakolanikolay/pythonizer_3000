import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE) as file:
        data = json.load(file)
        return round((sum([item["score"]*item["weight"] for item in data])), 3)


print(task())
