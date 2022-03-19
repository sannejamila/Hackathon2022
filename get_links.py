from load_json_data import load_json_data
from fetch_from_planetary import search, search_with_date
import requests
import json
import os

def get_links():
    data = load_json_data()

    links = set()
    length = len(data[::20])
    for i, reef in enumerate(data[::20]):
        print(i, "of", length)
        link_data = search({"coordinates": reef['geometry']['coordinates']}).get_all_items_as_dict()["features"]
        for link_dict in link_data:
            if (link_dict['properties']['eo:cloud_cover'] > 30):
                continue
            link = link_dict["assets"]["rendered_preview"]["href"]
            links.add(link)
    return links



def save_links(links, filename):
    print("Number of links", len(links))
    with open(filename, "w") as f:
        json.dump(list(links), f)
    print("Successfully saved links to", filename)

def load_links(filename):

    with open(filename, "r") as f:
        links = json.load(f)
    print(f"Successfully loaded {len((links))} links")
    return links

def download_pictures(links, data_folder):
    total_number = len(links)
    for i, pic in enumerate(links):
        try:
            print(f"downloading nr. {i} of {total_number}")
            img_data = requests.get(pic).content
            with open(os.path.join(data_folder, f'{i}_image_name.jpg'), 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print("error in download:", e)

    print("download complete")



if __name__ == "__main__":
    links = get_links()
    save_links(links, "data/links_cloudy.json")
    links = load_links("data/links_cloudy.json")
    download_pictures(links, "data/corals_cloudy")
    #
    # links = get_links()
    # print("Links have been secured")
    # download_pictures(links)
    # print("Pictures should have been downloaded")
