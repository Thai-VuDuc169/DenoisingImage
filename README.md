# Content
  - [Introduction](#introduction)
  - [Class Diagram](#class-diagram)
  - [Dataset](#dataset)
  - [Demo Program](#demo-program)
  - [Evaluation](#evaluation)

# Introduction
  :neckbeard: Denoising in the Cham inscription image :moyai:

# Class Diagram
  ![Class Diagram](https://github.com/Thai-VuDuc169/DenoisingImage/blob/main/Resource/Class%20Diagram.png)
  Please check out the full [link](https://app.diagrams.net/#G1fZkqfMjVfclW_PYTWd6XoM0FBFyusgkX)
# Dataset
  process raw data to conduct training for deep learning is done in [here](https://colab.research.google.com/drive/1STDX9iDza64d4sIixLN94dOuLy8obbWQ?usp=sharing) (run on colab). I proceeded to separate pairs of images in the Double_2021 for train and test set (without validation set). Processed data is saved in *hdf5 format. Check for more details: [My google drive](https://drive.google.com/drive/folders/1FtUPBOZl1PE_O9mU8Vl9V2OPjjAv367r?usp=sharing)
  ```
  DenoisingImage/Original_data/
        Clean         <images is cleand>
        Degraded      <images is degraded>
        Double_2021   <contain pairs of degraded and cleand images>
  ```
# Demo Program
  you can customize the parameters of filters based on BasicFilter.py and DenoiseUsingDL.py 
  Run Main.py to run the demo program
  ```
  python3 /<full_path>/Main.py
  ```
  ![Demo Program](https://github.com/Thai-VuDuc169/DenoisingImage/blob/main/Resource/Demo_v1.png)
# Evaluation
  - **SSIM (_Structural Similarity Index Measure_)**: is a method for predicting the perceived quality of digital television and cinematic pictures, as well as other kinds of digital images and videos. SSIM is used for measuring the similarity between two images. The SSIM index is a full reference metric; in other words, the measurement or prediction of image quality is based on an initial uncompressed or distortion-free image as reference. SSIM is a perception-based model that considers image degradation as perceived change in structural information, while also incorporating important perceptual phenomena, including both luminance masking and contrast masking terms. The difference with other techniques such as MSE or PSNR is that these approaches estimate absolute errors. [Reference for more details](https://en.wikipedia.org/wiki/Structural_similarity)
  - **PSNR (_Peak Signal-to-Noise Ratio_)**: is an engineering term for the ratio between the maximum possible power of a signal and the power of corrupting noise that affects the fidelity of its representation. Because many signals have a very wide dynamic range, PSNR is usually expressed as a logarithmic quantity using the decibel scale. [Reference for more details](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio#:~:text=Peak%20signal%2Dto%2Dnoise%20ratio%20(PSNR)%20is%20an,the%20fidelity%20of%20its%20representation.)

<img align="right" width="100" height="100" alt="fidget spinner" src="https://github.com/Thai-VuDuc169/DenoisingImage/blob/main/Resource/VortexClockSequencer.gif">
