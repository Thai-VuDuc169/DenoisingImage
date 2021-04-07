from skimage.metrics import peak_signal_noise_ratio, structural_similarity


class Evaluator:
    def __init__(self, input_img):
        self.base_image = input_img
    
    # Compute the peak signal to noise ratio (PSNR) for an image.
    def calcPSNR(self, image_test):
        return peak_signal_noise_ratio(image_true= self.base_image, 
                                        image_test= image_test,
                                        data_range= 255)

    def calcSSIM(self, image_test):
        return structural_similarity(im1= self.base_image,
                                        im2= image_test,
                                        data_range= 255)

    def evalImages(self, image_test):
        PSNR_value = self.calcPSNR(image_test)
        SSIM_value = self.calcSSIM(image_test)
        return PSNR_value, SSIM_value