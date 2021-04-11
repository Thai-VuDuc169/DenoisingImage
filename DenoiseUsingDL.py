from tensorflow.keras.models import load_model
from BasicFilters import Filter
import numpy as np
import cv2 as cv
class Autodecoder(Filter):
    def __init__ (self, link= r"TrainedModel/Autodecoder1.hdf5"):
        try: 
            super().__init__(load_model(link))
            print("load model successfully!")
        except:
            print ("fail")
    def __str__ (self):
        return "Autodecoder"
    
    def filterImage(self):
        temp_img = cv.resize(Filter.input_mat, (2048, 256 ), interpolation= cv.INTER_CUBIC)
        result = self.kernel.predict(temp_img.reshape((1,256,2048,1))) * 255
        result = result.reshape((256,2048,1))
        return result.astype(int)


