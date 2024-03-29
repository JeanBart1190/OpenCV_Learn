import cv2 as cv
import numpy as np

# img = np.zeros((512,512,3), np.uint8)
# img[:] = [0,255,255]
# cv.namedWindow('image')
# cv.imshow('image',img)
# cv.imwrite('..\\OutputFiles\\yellow.jpg',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

#img = cv.imread('..\\OutputFiles\\yellow.jpg')

cv.namedWindow('img', cv.WINDOW_NORMAL)
img = cv.imread('..\\src\\Rika_cry.png',cv.IMREAD_UNCHANGED)

print(img.shape)
print(img.size)
print(img.dtype)

#b,g,r,a = cv.split(img) #时间长
image = np.zeros_like(img)
face = img[30:60, 60:100]
img[10:40, 40:80] = face


cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
