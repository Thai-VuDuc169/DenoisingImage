from tensorflow.keras.models import load_model
from BasicFilters import Filter
import numpy as np

class Autodecoder(Filter):
    def __init__ (self, link= r"TrainedModel/Autodecoder1.hdf5"):
        super().__init__(load_model(link))
    
    def __str__ (self):
        return "Autodecoder"
    
    def filterImage(self):
        temp_img = np.resize(Filter.input_mat, (256,2048))
        result = self.kernel.predict(temp_img.reshape((1,256,2048,1))) * 255
        return result.astype(int)


