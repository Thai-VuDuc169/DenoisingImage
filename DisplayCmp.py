import matplotlib.pyplot as plt
import cv2 as cv
import sys
from EvaluateImages import Evaluator
from BasicFilters import Filter

assert ('win32' in sys.platform), "This code runs on Windows only."

class Display:
    def __init__ (self, filter_list, input_img, output_img):
        assert (all(isinstance(i,  Filter ) for i in filter_list)), "The list of filter is not instances of 'Filter' class"
        self.filter_list = filter_list
        self.input_img = input_img
        self.output_img = output_img
        Filter.setInputImage(input_img)

    def plotUsingMatplotlib(self): # sorted_by_PSNR= True):
        # {Key: [PSNR, SSIM]} -> Key: name of a filter (contain processed image); [PSNR and SSIM value] 
        # dic_images= {}
        # for i in self.filter_list:
        evaluator = Evaluator(self.output_img)
        plt.figure(figsize = (10, 80))
        
        plt.subplot((int(len(self.filter_list)/2) + 2), 2, 1)
        plt.title("INPUT IMAGE")
        plt.imshow(self.input_img, "gray")

        plt.subplot((int(len(self.filter_list)/2) + 2), 2, 2)
        plt.title("OUTPUT IMAGE")
        plt.imshow(self.output_img, "gray")

        for index, elem in enumerate(self.filter_list, 3):
            plt.subplot((int(len(self.filter_list)/2) + 2), 2, index)
            plt.title(elem)
            temp_img = elem.filterImage()
            plt.imshow(temp_img, "gray")
            plt.ylabel("SSIM: {0:.3}\nPSNR: {1:.3}"
                        .format(*evaluator.evalImages(temp_img)))
        plt.show()