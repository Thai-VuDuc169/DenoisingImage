import cv2 as cv
import numpy as np 

"""
If we have not defined the __str__, then it will call the __repr__ method. 
The __repr__ method returns a string that describes the pointer of the object by default 
(if the programmer does not define it).
"""
class Filter:
    def __init__(self, kernel):
        self.kernel = kernel
    
    def __str__ (self):
        return "Filter"
    
    def filterImage(self):
        pass

    @classmethod                    # staticmethod thì được dùng cho các utility hơn, ko liên quan đến các trạng thái của lớp 
    def setInputImage(cls, matrix):
        # cls.input_mat = matrix    # cls.input_mat: mỗi class cụ thể sẽ có 1 biến khác nhau (các lớp kế thừa sẽ có các biến khác nhau)
        Filter.input_mat = matrix   # <class_name>.input_mat: biến static chung cho toàn bộ lớp (các lớp kế thừa sẽ có chung biến với nhau)


class MeanFilter(Filter):
    def __init__ (self, kernel):
        # kernel is a tuple 
        super().__init__(kernel)

    def __str__ (self):
        return "Mean Filter"

    def filterImage(self): 
        return cv.blur(Filter.input_mat, self.kernel)

class MedianFilter(Filter):
    def __init__(self, kernel):
        # kernel is a odd interger
        super().__init__(kernel)

    def __str__(self):
        return "Median Filter"

    def filterImage(self):
        return cv.medianBlur(Filter.input_mat, self.kernel)

class GaussianBlur(Filter):
    def __init__(self, kernel):
        # kernel is a tuple
        super().__init__(kernel)

    def __str__(self):
        return "Gaussian Blur"

    def filterImage(self, signma_X= 0):
        return cv.GaussianBlur(Filter.input_mat, self.kernel, sigma_X)

class LaplacianFilter(Filter):
    def __init__(self, kernel):
        # kernel is a odd interger
        super().__init__(kernel)

    def __str__(self):
        return "Laplacian Filter"

    def filterImage(self):
        return cv.Laplacian(Filter.input_mat, cv.CV_64F, ksize= self.kernel)

class

