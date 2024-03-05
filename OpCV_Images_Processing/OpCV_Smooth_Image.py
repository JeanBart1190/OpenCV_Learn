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




if __name__ == '__main__' :
    #two_dimensional_convolution()
    pass