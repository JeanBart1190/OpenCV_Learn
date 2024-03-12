import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def canny():
    img = cv.imread('..\\src\\Perspective_Transform_test.png',0)
    img = cv.GaussianBlur(img,(5,5),0)
    edge = cv.Canny(img,100,200,True)
    plt.subplot(1,2,1), plt.imshow(img,cmap='gray'),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2), plt.imshow(edge,cmap='gray'),plt.title("Edge")
    plt.xticks([]),plt.yticks([])
    plt.show()


def test():
    img = cv.imread('..\\src\\sudoku.jpg', 0)
    img = cv.GaussianBlur(img, (5, 5), 0)

    nothing = lambda x: None
    cv.namedWindow('Compare',cv.WINDOW_NORMAL)
    cv.resizeWindow('Compare',img.shape[1]*2,img.shape[0]*2)
    cv.createTrackbar('minVal','Compare',1,255,nothing)
    cv.createTrackbar('maxVal','Compare',1,255,nothing)
    minVal, maxVal = 0, 0
    while(True):
        solve = lambda img : cv.Canny(cv.GaussianBlur(img, (5, 5), 0),minVal,maxVal,True)
        cv.imshow('Compare',solve(img))
        cv.waitKey(10) & 0xFF
        minVal = cv.getTrackbarPos('minVal','Compare')
        maxVal = cv.getTrackbarPos('maxVal','Compare')
    cv.destroyAllWindows()

if __name__ == '__main__':
    # canny()
    test()
    pass