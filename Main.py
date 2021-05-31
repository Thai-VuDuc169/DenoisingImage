from BasicFilters import *
from DisplayCmp import Display
from DenoiseUsingDL import Autodecoder
import cv2 as cv
import numpy as np
import cv2 as cv
import os
import random
random.seed(10) # or 1
import pathlib

current_folder_path = str(pathlib.Path(__file__).parent.absolute())
print("Hello {}!, the current folder path is '{}' in this system"
        .format(os.getlogin(), current_folder_path ))


random_file = random.choice(os.listdir(current_folder_path + "\\Original_data\\Degraded"))
in_img = cv.imread(current_folder_path + "\\Original_data\\Degraded\\" + random_file, 0)
out_img = cv.imread(current_folder_path + "\\Original_data\\Clean\\" + random_file, 0) 

mean_filter = MeanFilter()
median_filter = MedianFilter()
gaussian_blur = GaussianBlur()
laplacian_filter = LaplacianFilter()
opening_filter = OpeningFilter()
autodecoder = Autodecoder()
filter_list = [mean_filter, median_filter, gaussian_blur, laplacian_filter, opening_filter,autodecoder]

display = Display(filter_list, input_img= in_img, output_img= out_img)
display.plotUsingMatplotlib()
