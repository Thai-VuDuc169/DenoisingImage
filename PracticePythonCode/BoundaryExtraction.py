import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pathlib
import os


def extractInBound(img):     # Inner Boundary Extraction
        # create a corss kernel
        kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3,3))
        r=cv.erode(img,kernel,iterations=1)
        e=img-r
        return e
def extractOutBound(img):    # Outer Boundary Extraction
        # create a corss kernel
        kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3,3))
        d = cv.dilate(img,kernel,iterations=1)
        #Edge extraction
        e=d-img
        return e
def main():
        current_folder_path = str(pathlib.Path(__file__).parent.absolute())
        print("Hello {}!, the current folder path is '{}' in this system"
                .format(os.getlogin(), current_folder_path ))
        
        img = cv.imread(current_folder_path + "//TestConnectedComponent.png", 0) # GeomatryShape.jpeg
        _, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
        titles = [ 'INPUT IMAGE', 'INNER BOUNDARY EXTRACTION', 'OUTER BOUNDARY EXTRACTION']
        images = [img, extractInBound(img), extractOutBound(img)]
        for i in range(len(titles)):
                plt.subplot(2, 2, i+1)
                plt.title(titles[i])
                plt.imshow(images[i], "gray")
                plt.xticks(ticks=[])
                plt.yticks(ticks=[])
        plt.show()
if __name__ == "__main__":
        main()

