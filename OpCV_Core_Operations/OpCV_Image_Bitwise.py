import copy

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img1 = cv.imread('C:\\Users\\admin1\\Desktop\\c0b7f97433cc21a376dd1097c4004c58227238.png_720w_476h_1e_1c.png')
img2 = cv.imread('C:\\Users\\admin1\\Desktop\\8b8fabc088b99ca4571b60347edcff1adb85f689.png')



img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

img = copy.deepcopy(img1)
img_ = copy.deepcopy(img2)

rows, cols, channels = img2.shape
roi = img1 [0:rows, 0:cols]

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 0, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask = mask)

dst = cv.add(img1_bg, img2_fg)
img1 [0:rows, 0:cols] = dst


plt.subplot(331), plt.imshow(img, 'gray')
plt.subplot(332), plt.imshow(img_, 'gray')
plt.subplot(333), plt.imshow(img2gray, 'gray')
# plt.subplot(334), plt.imshow(ret, 'gray')
# plt.subplot(335), plt.imshow(mask, 'gray')
plt.subplot(334), plt.imshow(mask_inv, 'gray')
plt.subplot(335), plt.imshow(img1_bg, 'gray')
plt.subplot(336), plt.imshow(img2_fg, 'gray')
plt.subplot(337), plt.imshow(img1, 'gray')

plt.show()




