import json

def load_json_data(filename="data/benthic.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return [i for i in data]

if __name__ == "__main__":
    for coral_reef in load_json_data():
        print(coral_reef)