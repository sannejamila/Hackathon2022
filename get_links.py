from load_json_data import load_json_data
from fetch_from_planetary import search

def get_links():
    data = load_json_data()

    links = set()
    for reef in data[::20000]:
        link_data = search({"coordinates": reef['geometry']['coordinates']}).get_all_items_as_dict()["features"]
        for link_dict in link_data:
            if (link_dict['properties']['eo:cloud_cover'] > 5):
                continue
            link = link_dict["assets"]["rendered_preview"]["href"]
            links.add(link)
    return links

import requests
def download_pictures(links):
    for pic in links:
        img_data = requests.get(pic["assets"]["rendered_preview"]["href"]).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)

if __name__ == "__main__":
    links = get_links()
    print("Links have been secured")
    download_pictures(links)
    print("Pictures should have been downloaded")
