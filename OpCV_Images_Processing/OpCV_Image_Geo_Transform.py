import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def image_resize():
    img = cv.imread('..\\src\\Rika_normal.png')
    # res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
    res = cv.resize(img,None,fx=2,fy=2, interpolation = cv.INTER_AREA)
    cv.imshow('res', res)
    cv.waitKey(0)
    cv.destroyAllWindows()

def image_translation_transform():
    img = cv.imread('..\\src\\Rika_normal.png', cv.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    M = np.float32([[1, 0, -10], [0, 1, -50]])

    dst = cv.warpAffine(img, M, (cols, rows))
    #cv.warpAffine 函数的第三个参数是输出图像的大小，其形式应为（宽度、高度）。宽度=列数，高度=行数。

    plt.subplot(121), plt.imshow(img,'gray'), plt.title('Original')
    plt.subplot(122), plt.imshow(dst,'gray'), plt.title('Transformed')
    plt.show()

def image_rotation_transform():
    img = cv.imread('..\\src\\Rika_normal.png', cv.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    M = cv.getRotationMatrix2D(((cols-1)/10.0, (rows-1)/10.0), 45, 1)
    dst = cv.warpAffine(img, M, (cols,rows))
    plt.subplot(121), plt.imshow(img,'gray'), plt.title('Original')
    plt.subplot(122), plt.imshow(dst,'gray'), plt.title('Transformed')
    plt.show()

def image_affine_transform():
    img = cv.imread('..\\src\\Rika_normal.png')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols, channel = img.shape
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv.getAffineTransform(pts1,pts2)
    dst = cv.warpAffine(img,M,(cols,rows))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()

def image_Perspective_transform():
    img = cv.imread('..\\src\\Perspective_Transform_test.png')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rows, cols, channel = img.shape
    #用"画图"打开图片, 获得所需四个点的像素位置
    pts1 = np.float32([[7,248],[221,16],[311,372],[408,51]])
    pts2 = np.float32([[0,0],[500,0],[0,375],[500,375]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(img,M,(500,375))
    plt.subplot(121), plt.imshow(img), plt.title('input')
    plt.subplot(122), plt.imshow(dst), plt.title('output')
    plt.show()

if __name__ == '__main__' :
    #image_resize()
    #image_translation_transform()
    #image_rotation_transform()
    #image_affine_transform()
    image_Perspective_transform()
    pass

