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
    img = cv.cvtColor(cv.imread('..\\src\\Rika_cry.png'), cv.COLOR_BGR2RGB)
    Blur = cv.blur(img,(5,5))
    GaussianBlur = cv.GaussianBlur(img,(5,5),0)
    plt.subplot(221), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(Blur), plt.title('average_blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(GaussianBlur), plt.title('Gaussian_blur')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__' :
    #two_dimensional_convolution()
    blur()
    pass