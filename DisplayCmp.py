import matplotlib.pyplot as plt
import cv2 as cv
from EvaluateImages import Evaluator
from BasicFilters import Filter


class Display:
    def __init__ (self, filter_list, input_img, output_img):
        assert (all(isinstance(i,  Filter ) for i in filter_list)), "The list of filter is not instances of 'Filter' class"
        self.filter_list = filter_list
        self.input_img = input_img
        self.output_img = output_img
        Filter.setInputImage(input_img)

    def plotUsingMatplotlib(self):
        evaluator = Evaluator(self.output_img)
        plt.figure(figsize = (10, 80))
        
        plt.subplot((int(len(self.filter_list)/2) + 2), 2, 1)
        plt.title("INPUT IMAGE")
        plt.imshow(self.input_img, "gray")
        plt.xticks(ticks=[])
        plt.yticks(ticks=[])

        plt.subplot((int(len(self.filter_list)/2) + 2), 2, 2)
        plt.title("OUTPUT IMAGE")
        plt.imshow(self.output_img, "gray")
        plt.xticks(ticks=[])
        plt.yticks(ticks=[])

        for index, elem in enumerate(self.filter_list, 3):
            plt.subplot((int(len(self.filter_list)/2) + 2), 2, index)
            plt.title(elem)
            temp_img = elem.filterImage()
            plt.imshow(temp_img, "gray")
            plt.ylabel("PSNR: {0:.3} dB\nSSIM: {1:.3}"
                        .format(*evaluator.evalImages(temp_img)))
            plt.xticks(ticks=[])
            plt.yticks(ticks=[])
        plt.show()