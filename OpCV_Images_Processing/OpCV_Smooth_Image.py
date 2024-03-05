import random

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def two_dimensional_convolution():
    img = cv.cvtColor(cv.imread('..\\src\\Rika_cry.png'), cv.COLOR_BGR2RGB)
    kernel = np.ones((5,5),np.float32)/25
    dst = cv.filter2D(img, -1, kernel=kernel)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('2D dimensional')
    plt.xticks([]), plt.yticks([])
    plt.show()

def blur():
    img = cv.cvtColor(cv.imread('..\\src\\Turtle_surprise.png'), cv.COLOR_BGR2RGB)
    #均值模糊
    Blur = cv.blur(img,(5,5))
    #高斯模糊
    GaussianBlur = cv.GaussianBlur(img,(5,5),0)
    #添加噪声
    img_noise = addSaltAndPepperNoise(img,0.9)
    #中值滤波
    medianBlur = cv.medianBlur(img_noise,5)
    #双边滤波
    bilateral_filtering = cv.bilateralFilter(img_noise,9,75,75)


    plt.subplot(231), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(Blur), plt.title('average_blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(GaussianBlur), plt.title('Gaussian_blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234), plt.imshow(img_noise), plt.title('noise img')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(medianBlur), plt.title('median_blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(bilateral_filtering), plt.title('bilaterl_Filter')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 中值滤波  cv.medianBlur()
# 双边滤波  cv.bilaterlFilter()


def addSaltAndPepperNoise(img, salt_prob):
    img_copy = img.copy()
    rows , cols, channels = img_copy.shape
    for i in range(rows) :
        for j in range(cols) :
            pepper_prob = random.random()
            if pepper_prob < salt_prob :
                if random.random() > 0.5 :
                    img_copy[i][j] = 0 ##salt
                else :
                    img_copy[i][j] = 255 ##pepper
    return img_copy



if __name__ == '__main__' :
    #two_dimensional_convolution()
    blur()
    pass