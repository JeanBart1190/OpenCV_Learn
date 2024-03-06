import cv2 as cv
import numpy as np
from matplotlib import  pyplot as plt

def MorphOps():
    img1 = cv.cvtColor(cv.imread('..\\src\\Morphological_test.png'),cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(cv.imread('..\\src\\Morphological_test2.png'),cv.COLOR_BGR2RGB)
    img3 = cv.cvtColor(cv.imread('..\\src\\Morphological_test3.png'),cv.COLOR_BGR2RGB)



    kernel = np.ones((5,5),np.float32)/25

    ##腐蚀
    erode = cv.erode(img1,kernel,iterations=1)
    ##膨胀
    dilation = cv.dilate(img1,kernel,iterations=1)
    ##开运算 (先腐蚀后膨胀)
    opening = cv.morphologyEx(img2,cv.MORPH_OPEN,kernel)
    ##闭运算 (先膨胀后腐蚀)
    closing = cv.morphologyEx(img3,cv.MORPH_CLOSE,kernel)
    ##形态梯度(膨胀与腐蚀之间的差值)
    gradient = cv.morphologyEx(img1,cv.MORPH_GRADIENT,kernel)
    ##顶帽(原图像与原图像开运算后的差值)
    tophat = cv.morphologyEx(img1,cv.MORPH_TOPHAT,np.ones((7*7),np.float32)/49)
    ##黑帽(原图像与原图像闭运算后的差值)
    blackhat = cv.morphologyEx(img1,cv.MORPH_BLACKHAT,kernel)

    plt.subplot(2,5,1), plt.imshow(img1), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,2), plt.imshow(erode), plt.title('Erode')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,3), plt.imshow(dilation), plt.title('Dilation')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,4), plt.imshow(img2), plt.title('Img2')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,5), plt.imshow(opening), plt.title('Opening')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,6), plt.imshow(img3), plt.title('Img3')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,7), plt.imshow(closing), plt.title('Closing')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,8), plt.imshow(gradient), plt.title('Gradient')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,9), plt.imshow(tophat), plt.title('Tophat')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2,5,10), plt.imshow(blackhat), plt.title('Blackhat')
    plt.xticks([]), plt.yticks([])

    plt.show()

def struct_element():
    ##矩形结构元素
    print(cv.getStructuringElement(cv.MORPH_RECT, (5,5)))
    ##椭圆形结构元素
    print(cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5)))
    ##十字形结构元素
    print(cv.getStructuringElement(cv.MORPH_CROSS, (5,5)))

if __name__ == '__main__':
    MorphOps()
    struct_element()
    pass
