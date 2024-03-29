import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def gradient_cal():
    img = cv.imread('..\\src\\sudoku.jpg',0)
    img = mage_Perspective_transform(img)
    ##Laplacian微分
    laplacian = cv.Laplacian(img,cv.CV_64F,ksize=9,borderType=cv.BORDER_REFLECT,scale=0.5)

    ##Sobel微分
    sobelx = cv.Sobel(img,cv.CV_32F, 1, 0, ksize=5)
    sobely = cv.Sobel(img,cv.CV_32F, 0, 1, ksize=5)

    plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 5), plt.imshow(cv.bitwise_and(sobelx,sobely),cmap='gray')
    plt.title('mix'), plt.xticks([]), plt.yticks([])
    plt.show()

def mage_Perspective_transform(img):
    pst1 = np.float32([[185,20],[467,70],[141,321],[422,345]])
    pst2 = np.float32([[0,0],[500,0],[0,500],[500,500]])
    M = cv.getPerspectiveTransform(pst1,pst2)
    return cv.warpPerspective(img,M,(500,500))

def compare_different_scale():
    cv.namedWindow('Compare')

    nothing = lambda x: None
    on_trackbar= lambda  val: None if val%2 == 0 else None
    cv.createTrackbar('ksize','Compare',3,11,on_trackbar)
    # cv.createTrackbar('scale','Compare',1,10,nothing)
    # cv.createTrackbar('delta','Compare',0,10,nothing)

    while(True):

        k = cv.waitKey(100) &0xFF

        if k == 27 :
            break
        ksize = cv.getTrackbarPos('ksize','Compare')
        # scale = cv.getTrackbarPos('scale','Compare')
        # delta = cv.getTrackbarPos('delta','Compare')

        img =  cv.Laplacian(cv.imread('..\\src\\sudoku.jpg'), cv.CV_64F, ksize=ksize)
        cv.imshow('Compare',img)
    cv.destroyAllWindows()

if __name__ == '__main__' :
    gradient_cal()
    # compare_different_scale()
    pass