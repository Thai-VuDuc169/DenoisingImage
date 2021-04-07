import random
# random.seed(11)
import numpy as np
import cv2 as cv
import os
from BasicFilters import Filter, MeanFilter, MedianFilter, LaplacianFilter, OpeningFilter
from DenoiseUsingDL import Autodecoder
import matplotlib.pyplot as plt


kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))

path = r"Original_data\Degraded"
random_file = random.choice(os.listdir(path))
img = cv.imread(path + "\\"  + random_file , 0)

Filter.setInputImage(img)
mean_filter = LaplacianFilter()

opening_filter = OpeningFilter()
auto = Autodecoder()

# cv.imshow("asdf", opening_filter.filterImage())
# cv.imshow("autodecoder", auto.filterImage()[0,:,:,:] )
plt.imshow(auto.filterImage()[0,:,:,:], "gray")
cv.imshow("origin", img)

cv.waitKey(0)
cv.destroyAllWindows()

