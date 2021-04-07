from BasicFilters import *
from cv2 import cv2 as cv
import numpy as np
import cv2 as cv
import os
import random
random.seed(10)
import matplotlib.pyplot as plt

path = r"E:\20202\Image Processing\DenoisingImage\Original_data\Degraded"
random_file = random.choice(os.listdir(path))
img = cv.imread(path + "\\"  + random_file , 0)

Filter.setInputImage(img)
mean_filter = MeanFilter()
median_filter = MedianFilter()
gaussian_blur = GaussianBlur()
laplacian_filter = LaplacianFilter()

filter_list = [mean_filter, median_filter, gaussian_blur, laplacian_filter]
for index, e in enumerate(filter_list, 1):
    plt.subplot()
    plt.imshow( i.filterImage())
    plt.
    
plt.show()
