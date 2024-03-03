import cv2 as cv
import numpy as np

img1 = cv.imread('C:\\Users\\admin1\\Desktop\\8b8fabc088b99ca4571b60347edcff1adb85f689.png')
img2 = cv.imread('C:\\Users\\admin1\\Desktop\\e6119c61f4e03307d19ea3ff449a03e183d2b964.png')

dst = cv.addWeighted(img1, 0.8, img2, 0.2, 20)

dst2 = cv.add(img1,img2)

cv.namedWindow('img')
cv.imshow('img',dst2)
cv.waitKey(0)
cv.destroyAllWindows()