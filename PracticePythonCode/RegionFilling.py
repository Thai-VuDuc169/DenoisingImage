import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pathlib
import os
import time
from scipy import ndimage


current_folder_path = str(pathlib.Path(__file__).parent.absolute())
print("Hello {}!, the current folder path is '{}' in this system"
        .format(os.getlogin(), current_folder_path ))
       
I = cv.imread(current_folder_path + "//TestFilling.png", 0)
_, img = cv.threshold(I, 127, 255, cv.THRESH_BINARY_INV)

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        fname = func.__name__
        print( "{0} took {1:.15f} seconds to execute!".format(fname, after-before))
        return value
    return wrapper


@timed
def wrapBinaryFillHoles(img):
        return ndimage.binary_fill_holes(img).astype(int)

@timed
def wrapFillRegion(img):
        def findStartPoint(img):
                h, w = img.shape
                x = np.zeros_like(img)
                for i in range(h):
                        for j in range(w):
                                if (i-1) == -1 or (j-1) == -1 :
                                        continue
                                if img[i][j-1] == 255 and img[i-1][j] == 255:
                                        x[i][j] = 255
                                        return x
        def fillRegion(img):
                # take complement matrix
                comp_img = np.copy(~img)
                kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3,3))
                start_matrix = findStartPoint(img)
                prior = (cv.dilate(start_matrix, kernel,iterations=1)) & comp_img
                print ((start_matrix != prior).any())
                while ((start_matrix != prior).any()):
                        start_matrix = np.copy(prior)
                        prior = (cv.dilate(start_matrix, kernel,iterations=1)) & comp_img
                return prior | img
        return fillRegion(img)

titles = [ 'INPUT IMAGE', 'FILLING REGION', 'BINARY_FILL_HOLES']
images = [img, wrapFillRegion(img), wrapBinaryFillHoles(img) ]
for i in range(len(titles)):
        plt.subplot(2, 2, i+1)
        plt.title(titles[i])
        plt.imshow(images[i], "gray")
        plt.xticks(ticks=[])
        plt.yticks(ticks=[])
plt.show()