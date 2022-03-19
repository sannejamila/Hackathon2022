import cv2
from PIL import Image
import os, os.path

path1 = "C:\\Users\\Eier\\OneDrive\\Bilder\\katter"
path2 = "C:\\Users\\Eier\\OneDrive\\Bilder\\katter2"

def flip_pictures(path1,path2):
    orientations = [1,0,-1]
    for f in os.listdir(path1):
        im = cv2.imread(path1 + "\\" + f)
        for i in orientations:
            flipped_image= cv2.flip(im, i)
            string = path2 + "\\" + str(i) + f 
            cv2.imwrite(string, flipped_image)


flip_pictures(path1,path2)

