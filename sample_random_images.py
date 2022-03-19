from global_land_mask import globe
from random import uniform
from fetch_from_planetary import search
from get_links import load_links, download_pictures, save_links


def sample_random_images(top_left_corner, bottom_right_corner, num, coral_links, batch_size=50):
    l, t, r, b = (*top_left_corner, *bottom_right_corner)

    num_coords = 0
    links = set()
    while len(links) < num:
        batch = [[]]
        for i in range(batch_size):

            x = uniform(l, r)
            y = uniform(t, b)

            if not globe.is_land(x, y):
                batch[0].append([y, x])
        link_data = search({"coordinates": batch}).get_all_items_as_dict()["features"]
        for link_dict in link_data:
            link = link_dict["assets"]["rendered_preview"]["href"]
            if link not in coral_links:
                links.add(link)
        print(len(links), "of", num)

    return links

if __name__ == "__main__":
    links = sample_random_images((-10.822170746118468, 137.92321102215595), (-17.706255347155274, 141.75589144731404), 3000, {"https::/empty.link"})
    save_links(links, "data/ocean_links.json")
    links = load_links("data/ocean_links.json")
    download_pictures(links, "data/ocean")