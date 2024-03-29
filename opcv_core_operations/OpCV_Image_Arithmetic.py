import cv2 as cv
import numpy as np

img1 = cv.imread('..\\src\\Rika_cry.png')
img2 = cv.imread('..\\src\\Rika_flower.png')

dst = cv.addWeighted(img1, 0.8, img2, 0.2, 20)

dst2 = cv.add(img1,img2)

cv.namedWindow('img')
cv.imshow('img',dst2)
cv.waitKey(0)
cv.destroyAllWindows()