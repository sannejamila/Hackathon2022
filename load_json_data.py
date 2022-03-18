import json
import fetch_from_planetary

def load_json_data(filename="data/benthic.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return [i for i in data]

if __name__ == "__main__":
    coral_reef = load_json_data()[12341]
    #for i in range(300):
     #   print(fetch_from_planetary.search({"coordinates": coral_reef['geometry']['coordinates']}).get_all_items_as_dict()["features"][i]["assets"]["rendered_preview"])
    print(fetch_from_planetary.search({"coordinates": coral_reef['geometry']['coordinates']}).get_all_items_as_dict()["features"][0])
    #for coral_reef in load_json_data():
    #   print(coral_reef)

    #print(len(load_json_data()))