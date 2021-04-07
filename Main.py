from BasicFilters import *
import cv2 as cv
import numpy as np
import cv2 as cv
import os
import random
random.seed(10)
import matplotlib.pyplot as plt
import pathlib

current_folder_path = str(pathlib.Path(__file__).parent.absolute())
print("Hello {}!, the current folder path is '{}' in this system"
        .format(os.getlogin(), current_folder_path ))

random_file = random.choice(os.listdir(current_folder_path))
img = cv.imread(current_folder_path + "\\"  + random_file , 0)

Filter.setInputImage(img)
mean_filter = MeanFilter()
median_filter = MedianFilter()
gaussian_blur = GaussianBlur()
laplacian_filter = LaplacianFilter()
opening_filter = OpeningFilter()

filter_list = [mean_filter, median_filter, gaussian_blur, laplacian_filter]


plt.subplot((int(len(dir_folder)/2) + 2), 2, 1)
plt.title("INPUT IMAGE")
plt.imshow(self.input_img)
for index, e in enumerate(filter_list, 1):
    plt.subplot()
    plt.imshow(i.filterImage())
    # plt.
    
plt.show()
