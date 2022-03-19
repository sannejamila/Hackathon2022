from load_json_data import load_json_data
from fetch_from_planetary import search, search_with_date
import requests
import json
import os
from collections import defaultdict


def get_links_with_date(date):
    data = load_json_data()

    coordinates = set()
    link_place = defaultdict(list)
    links = set()
    length = len(data[::10000])
    for i, reef in enumerate(data[::10000]):
        print(i, "of", length)
        link_data = search_with_date(date, {"coordinates": reef['geometry']['coordinates']}).get_all_items_as_dict()["features"]
        for link_dict in link_data:
            if (link_dict['properties']['eo:cloud_cover'] > 30):
                continue
            link = link_dict["assets"]["rendered_preview"]["href"]
            links.add(link)
            temp = list()
            for value in link_dict['bbox']:
                temp.append(round(value))
            temp = tuple(temp)
            link_place[temp].append(link)
    return links, link_place



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

def download_pictures_with_dates(links, data_folder, date):
    total_number = len(links)
    for i, pic in enumerate(links):
        try:
            print(f"downloading nr. {i} of {total_number}")
            img_data = requests.get(pic).content
            with open(os.path.join(data_folder, f'{i}_image_name_date_20{date}.jpg'), 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print("error in download:", e)
    print("download complete")

def download_pictures_with_dates_and_place(links, data_folder, date, dic_place):
    total_number = len(links)
    for name, vari in dict(dic_place).items():
        os.makedirs(f"data/dated_images/date_20{date}/place_nr_{name}", exist_ok=True)

    for key, value in dict(dic_place).items():
        print(value)
        for i, link in enumerate(value):
            img_data = requests.get(link).content
            with open(os.path.join(data_folder, f'place_nr_{key}/{i}_image_name_date_20{date}.jpg'),
                      'wb') as handler:
                handler.write(img_data)
        """
        for j, link in enumerate(value):
            with open(os.path.join(data_folder, f'place_nr_{key}/{pic_count}_image_name_date_20{date}.jpg'), 'wb') as handler:
                print(link)
                pic_count+=1
"""
    """
    for i, pic in enumerate(links):
        try:
            print(f"downloading nr. {i} of {total_number}")
            pic_data = requests.get(pic).content
            with open(os.path.join(data_folder, f'{i}_image_name_date_20{date}.jpg'), 'wb') as handler:
                for key, value in dic_place:
                    handler.write(pic_data)

        except Exception as e:
            print("error in download:", e)
    print("download complete")
"""
if __name__ == "__main__":
    for date in range(13,21):
        links, links_place = get_links_with_date(date)
        save_links(links, "data/links_cloudy.json")
        links = load_links("data/links_cloudy.json")
        os.makedirs(f"data/dated_images/date_20{date}", exist_ok=True)
        download_pictures_with_dates_and_place(links, f"data/dated_images/date_20{date}", date, links_place)
