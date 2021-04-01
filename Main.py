from BasicFilters import Filter, MeanFilter, MedianFilter, LaplacianFilter, OpeningFilter
import cv2 as cv
import numpy as np
import os
import random
random.seed(10)

kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))

path = r"Original_data\Degraded"
random_file = random.choice(os.listdir(path))
img = cv.imread(path + "\\"  + random_file , 0)

Filter.setInputImage(img)
mean_filter = LaplacianFilter()

opening_filter = OpeningFilter()

cv.imshow("origin", img)
cv.imshow("asdf", opening_filter.filterImage())

cv.waitKey(0)
cv.destroyAllWindows()

