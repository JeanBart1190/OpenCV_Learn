import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

img1 = cv.cvtColor( cv.imread('..\\src\\Rika_cry.png'), cv.COLOR_BGR2RGB)
plt.subplot(221), plt.imshow(img1, 'gray'), plt.title('Original')
plt.subplot(222), plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2GRAY),'gray'), plt.title('RGB_to_GRAY')
plt.subplot(223), plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2HSV),'gray'), plt.title('RGB_to_HSV')
plt.show()