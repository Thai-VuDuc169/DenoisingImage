from tensorflow.keras.models import load_model
from BasicFilters import Filter
import numpy as np
import cv2 as cv

class Autodecoder(Filter):
    def __init__ (self, link= r"TrainedModel/Autodecoder1.hdf5"):
        try: 
            super().__init__(load_model(link))
        except:
            print ("load Autodecoder model is failed")

    def __str__ (self):
        return "Autodecoder"
    
    def filterImage(self):
        temp_img = cv.resize(Filter.input_mat, (2048, 256), interpolation= cv.INTER_CUBIC)
        result = self.kernel.predict(temp_img.reshape((1,256,2048,1))) * 255
        result = result.reshape((256,2048))
        result = np.uint8(result)
        result = cv.resize(result, (Filter.input_mat.shape[1], Filter.input_mat.shape[0]), 
                        interpolation= cv.INTER_CUBIC)
        # print("{}: type {}; {}: type {}".format(result.shape, result.dtype,
        #         Filter.input_mat.shape, Filter.input_mat.dtype))
        return result


