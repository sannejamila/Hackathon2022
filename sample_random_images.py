from global_land_mask import globe
from random import uniform
from fetch_from_planetary import search

def sample_random_images(top_left_corner, bottom_right_corner, num, coral_links, batch_size=50):
    l, t, r, b = (*top_left_corner, *bottom_right_corner)

    num_coords = 0
    links = set()
    while num_coords < num:
        batch = [[]]
        for i in range(batch_size):

            x = uniform(l, r)
            y = uniform(t, b)

            if not globe.is_land(x, y):
                batch[0].append([y, x])
        print("start")
        print("Coords", batch)
        link_data = search({"coordinates": batch}).get_all_items_as_dict()["features"]
        print("end")
        print(link_data)
        for link_dict in link_data:
            link = link_dict["assets"]["rendered_preview"]["href"]
            print(link)
            if link not in coral_links:
                print("include")
                links.add(link)
                num_coords += 1

    return links

if __name__ == "__main__":
    links = sample_random_images((-12.809395673491847, 139.2690916581671), (-17.706255347155274, 141.75589144731404), 8, {"https::/empty.link"})
    print(links)