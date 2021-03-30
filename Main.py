from BasicFilters import Filter, MeanFilter, MedianFilter, LaplacianFilter
import cv2 as cv
import numpy as np
import os
import random
random.seed(10)

path = r"E:\20202\Image Processing\Project3\Original_data\Degraded"
random_file = random.choice(os.listdir(path))
img = cv.imread(path + "\\"  + random_file , 0)

Filter.setInputImage(img)
mean_filter = LaplacianFilter(3)

cv.imshow("asdf", mean_filter.filterImage() )

cv.waitKey(0)
cv.destroyAllWindows()

