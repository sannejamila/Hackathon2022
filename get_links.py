from load_json_data import load_json_data
from fetch_from_planetary import search
import requests
import json
import os

def get_links():
    data = load_json_data("data/benthicred.json")

    links = set()
    length = len(data[::800])
    for i, reef in enumerate(data[::800]):
        print(i, "of", length)
        link_data = search({"coordinates": reef['geometry']['coordinates']}).get_all_items_as_dict()["features"]
        for link_dict in link_data:
            if (link_dict['properties']['eo:cloud_cover'] > 15):
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

def athread(links, numberc):
    download_pictures(links, "data/corals_cloudy" + str(numberc))


if __name__ == "__main__":
    import threading
    links = set(load_links("data/links_cloudy_caribbean.json"))
    for i in range(2,23):
        try:
            links.union(load_links("data/links" + str(i) + "_cloudy_caribbean.json"))
        except:
            pass
    links = list(links)
    print(len(links))
    t1 = threading.Thread(target=(lambda: download_pictures(links[0:500], "data/corals_cloudy1")), name="a")
    t2 = threading.Thread(target=(lambda: download_pictures(links[500:1000], "data/corals_cloudy2")), name="b")
    t3 = threading.Thread(target=(lambda: download_pictures(links[1000:1500], "data/corals_cloudy3")), name="c")
    t4 = threading.Thread(target=(lambda: download_pictures(links[1500:2000], "data/corals_cloudy4")), name="d")
    t5 = threading.Thread(target=(lambda: download_pictures(links[2000:2500], "data/corals_cloudy5")), name="e")
    t6 = threading.Thread(target=(lambda: download_pictures(links[2500:3000], "data/corals_cloudy6")), name="f")
    t7 = threading.Thread(target=(lambda: download_pictures(links[3000:3500], "data/corals_cloudy7")), name="g")
    t8 = threading.Thread(target=(lambda: download_pictures(links[3500:4000], "data/corals_cloudy8")), name="h")
    t9 = threading.Thread(target=(lambda: download_pictures(links[4000:4500], "data/corals_cloudy9")), name="i")
    t10 = threading.Thread(target=(lambda: download_pictures(links[4500:5000], "data/corals_cloudy10")), name="j")
    t11 = threading.Thread(target=(lambda: download_pictures(links[5000:5500], "data/corals_cloudy11")), name="k")
    t12 = threading.Thread(target=(lambda: download_pictures(links[5500:6000], "data/corals_cloudy12")), name="l")

    t1.start()
    t2.start()
    print("t")
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()

    #links = get_links()
    #save_links(links, "data/links_cloudy_red.json")
    #links = load_links("data/links_cloudy_red.json")
    #download_pictures(links, "data/corals_cloudy_red")
    #
    # links = get_links()
    # print("Links have been secured")
    # download_pictures(links)
    # print("Pictures should have been downloaded")
