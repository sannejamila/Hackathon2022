import json
import fetch_from_planetary

def load_json_data(filename="data/benthic.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return [i for i in data]

if __name__ == "__main__":
    coral_reef = load_json_data()[12341]
    print(fetch_from_planetary.search({"coordinates": coral_reef['geometry']['coordinates']}).get_all_items_as_dict())