import random

import cv2
import numpy as np
import os
import scipy
from scipy import signal

def detect_corals_in_image(img, display=False, calc_average=False, return_image=False):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([80,160,90])
    upper_blue = np.array([110,255,230])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel_size = 10
    freq_x = signal.windows.gaussian(kernel_size, std=2)*3
    freq_y = signal.windows.gaussian(kernel_size, std=2)*3
    kernel = np.array([[x*y for x in freq_x] for y in freq_y]).astype("uint8")
    mask = cv2.dilate(mask, kernel)
    mask = cv2.erode(mask, kernel)
    reef_size = np.sum(mask)
    res = cv2.bitwise_and(img, img, mask=mask)
    hsv = cv2.bitwise_and(hsv, hsv, mask=mask)
    average = np.zeros((3))
    print(hsv.shape)
    if (calc_average):
        count = 0
        for column in hsv:
            for row in column:
                if (row[2]):
                    count += 1
                    average += row
        if (count):
            average/=count

    if display:
        cv2.imshow("Before and after", img)
        cv2.waitKey()

        cv2.imshow("Before and after", res)
        cv2.waitKey()
    if return_image:
        return res
    return reef_size,average

def red_ring_image(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([80,160,90])
    upper_blue = np.array([110,255,230])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    reef_size = np.sum(mask)
    cv2.imwrite("mask_hue.jpg", mask)
    kernel_size = 75
    freq_x = signal.windows.gaussian(kernel_size, std=4)*3
    freq_y = signal.windows.gaussian(kernel_size, std=4)*3
    kernel = np.array([[x*y for x in freq_x] for y in freq_y]).astype("uint8")
    kernel_size2 = 4
    freq_x = signal.windows.gaussian(kernel_size2, std=2)*3
    freq_y = signal.windows.gaussian(kernel_size2, std=2)*3
    kernel2 = np.array([[x*y for x in freq_x] for y in freq_y]).astype("uint8")
    mask = cv2.dilate(mask, kernel)
    mask = cv2.dilate(mask, kernel)
    mask = cv2.dilate(mask, kernel)

    cv2.imwrite("mask_mask.jpg", mask)

    mask = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel2)

    cv2.imwrite("mask_outline.jpg", mask)


    res = img - cv2.bitwise_and(img, img, mask=mask)
    red = np.zeros(img.shape)
    red[:,:] = np.array([.21,.31,.7])*32
    res = res+red*cv2.bitwise_and(red, red, mask=mask)
    cv2.imwrite("mask_finished.jpg", res)
    #cv2.imshow("awdawd", red*cv2.bitwise_and(red, red, mask=mask))
    #cv2.waitKey()
    average = np.zeros((3))
    return res, reef_size

def get_paths(folder_name):
    return [os.path.join(folder_name, path) for path in os.listdir(folder_name)]

def get_reef_sizes(paths, display=False, calc_average=False):
    for path in paths:
        print(path)
        try:
            image = cv2.imread(path)
            reef_size, color = detect_corals_in_image(image, display, calc_average)
            reef_data.append({"path": path, "size": reef_size, "avg_color": color})
            print("Reef size:", reef_size, "color:", color)
        except Exception as e:
            print("Error with", path, e)
    return sorted(reef_data, key=lambda x:x["size"], reverse=True )

def evaluate_coral_extractor(coral_paths, ocean_paths, threshold, calc_average=False):
    coral_sizes = get_reef_sizes(coral_paths, calc_average)
    total_coral = len(coral_sizes)
    ocean_sizes = get_reef_sizes(ocean_paths, calc_average)
    total_ocean = len(ocean_sizes)
    total = total_coral+total_ocean
    total_correct = 0
    total_correct_coral = 0
    for coral in coral_sizes:
        if coral["size"] >= threshold:
            total_correct_coral+= 1
        else:
            break
    total_correct_ocean = 0
    for ocean in ocean_sizes:
        if ocean["size"] < threshold:
            total_correct_ocean += 1
    return total_correct_coral+total_correct_ocean, total, total_correct_coral, total_correct_ocean

if __name__ == "__main__":
    parent_coral = "C:/Users/espen/Documents/data/corals/corals"
    parent_ocean = "C:/Users/espen/Documents/data/ocean/ocean"
    coral_paths = get_paths(parent_coral)
    ocean_paths = get_paths(parent_ocean)
    reef_data = []
    print(coral_paths)
    print(ocean_paths)
    concatted = coral_paths+ocean_paths
    random.shuffle(concatted)
    #print(evaluate_coral_extractor(coral_paths, ocean_paths, 1500))

    sizes = get_reef_sizes(coral_paths, display=True)

    for reef_data in sizes:
        cv2.imshow("awda", cv2.imread(reef_data["path"]))
        cv2.waitKey()