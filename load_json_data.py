import json
import fetch_from_planetary
import pystac

def load_json_data(filename="data/benthic.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return [i for i in data]

if __name__ == "__main__":
    aset = set()
    for coral_reef in load_json_data()[::1000]:
        fetched = fetch_from_planetary.search({"coordinates": coral_reef['geometry']['coordinates']}).get_all_items_as_dict()['features']
        for fetch in fetched:
            if(fetch['properties']['eo:cloud_cover'] > 5):
                continue
            aset.add(fetch['assets']['rendered_preview']['href'])
        #print(fetch_from_planetary.search({"coordinates": coral_reef['geometry']['coordinates']}).get_all_items_as_dict())
    print(aset, "\n", len(aset))