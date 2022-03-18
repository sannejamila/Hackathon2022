from load_json_data import load_json_data
from fetch_from_planetary import search

def get_links():
    data = load_json_data()

    links = set()
    for reef in data[::20000]:
        link_data = search({"coordinates": reef['geometry']['coordinates']}).get_all_items_as_dict()["features"]
        for link_dict in link_data:
            link = link_dict["assets"]["rendered_preview"]["href"]
            print(link)
            links.add(link)
    return links


if __name__ == "__main__":
    get_links()