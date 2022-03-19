import os

from global_land_mask import globe
from random import uniform
from fetch_from_planetary import search
from get_links import load_links, download_pictures, save_links


def sample_random_images(top_left_corner, bottom_right_corner, num, coral_links, batch_size=50):
    l, t, r, b = (*top_left_corner, *bottom_right_corner)

    num_coords = 0
    links = set()
    print("Halla")
    while len(links) < num:
        batch = [[]]
        for i in range(batch_size):

            x = uniform(l, r)
            y = uniform(t, b)

            if not globe.is_land(x, y):
                batch[0].append([y, x])
        print("search")
        link_data = search({"coordinates": batch}).get_all_items_as_dict()["features"]
        print("searchend")
        for link_dict in link_data:
            link = link_dict["assets"]["rendered_preview"]["href"]
            if link not in coral_links:
                links.add(link)
        print(len(links), "of", num)

    return links

if __name__ == "__main__":
    links = sample_random_images((45.56794039153187, 164.79086620168565), (27.918165561879146, -165.96225727163014), 2300, {"https::/empty.link"})
    save_links(links, "data/ocean_links3.json")
    links = load_links("data/ocean_links3.json")
    os.makedirs("data/ocean3", exist_ok=True)
    download_pictures(links, "data/ocean3")
    #-5.289254923198517, 114.32078803511483
    #-3.0940141936830634, 109