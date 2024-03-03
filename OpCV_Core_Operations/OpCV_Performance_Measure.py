import time

import cv2 as cv
import numpy as np

img1 = cv.imread('..\\src\\RikaNya.png')
e1 = cv.getTickCount()
# start = time.time()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1,i)
# end = time.time()
e2 = cv.getTickCount()
t = (e2-e1) / cv.getTickFrequency()
print(t)
print(cv.useOptimized())
