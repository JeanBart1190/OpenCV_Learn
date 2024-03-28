import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class histogram_in_OpCV :
    def __init__(self, img):
        self.image = img

    def hist_gray(self):
        img = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        hist = cv.calcHist([img], [0], None, [256], [0,256])
        plt.figure(figsize=(10,6), dpi=100)
        plt.plot(hist)
        plt.grid()
        plt.show()

    def hist_gray_in_mat(self):
        img = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        plt.hist(img.ravel(), 256, [0,256])
        plt.show()

    def hist_brg_in_mat(self):
        img = self.image
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            hist = cv.calcHist([img], [i], None, [256], [0,256])
            plt.plot(hist, color = col)
            plt.xlim([0,256])
        plt.grid()
        plt.show()

    def hist_use_mask(self):
        img = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)


        mask = np.zeros(img.shape[:2], np.uint8)

        # 创建位于图片中心的掩膜
        # rows, cols= img.shape
        # center = np.array(self.image.shape[:2]) // 2
        # alpha = int(rows/4)+int(rows/10)
        # beta = int(cols/4)+int(rows/10)
        # mask[center[0]-alpha:center[0]+alpha,  center[1]-beta:center[1]+beta] = 255

        # 创建定位于人物的掩膜
        mask[2700:4300, 5400:6700] = 255

        masked_img = cv.bitwise_and(img, img, mask=mask)
        hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
        hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])
        plt.subplot(221), plt.imshow(img, 'gray')
        plt.subplot(222), plt.imshow(mask, 'gray')
        plt.subplot(223), plt.imshow(masked_img, 'gray')
        plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
        plt.xlim([0, 256])
        plt.show()

    def hist_equal(self):
        img = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        dst = cv.equalizeHist(img)

        hist_img = cv.calcHist(img, [0], None, [256], [0,256])
        hist_dist = cv.calcHist(dst, [0], None, [256], [0,256])

        plt.figure(figsize=(8, 8), dpi=120)
        plt.subplot(3, 2, 1), plt.imshow(img, 'gray'), plt.title('original')
        plt.subplot(3, 2, 2), plt.imshow(dst, 'gray'), plt.title('equal')
        plt.subplot(3, 2, 3), plt.plot(hist_img), plt.title('original hist')
        plt.subplot(3, 2, 4), plt.plot(hist_dist), plt.title('dist hist')
        plt.subplot(3, 2, 5), plt.imshow(np.hstack((img,dst))), plt.title('compare')
        plt.tight_layout()
        plt.show()

    def hist_equal_CLAHE(self):
        img = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

        clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        cl1 = clahe.apply(img)

        hist_img = cv.equalizeHist(img)

        plt.figure(figsize=(8, 8), dpi=120)
        plt.subplot(2, 3, 1), plt.imshow(img, 'gray'), plt.title('original')
        plt.subplot(2, 3, 2), plt.imshow(cl1, 'gray'), plt.title('clahe hist')
        plt.subplot(2, 3, 3), plt.imshow(hist_img, 'gray'), plt.title('normal hist')
        plt.subplot(2, 1, 2), plt.imshow(np.hstack((hist_img, cl1)), 'gray'), plt.title('normal_hist    compare    clahe_hist')
        plt.tight_layout()

        plt.show()

    # 2D 直方图 每个像素的色相和饱和度
    def hist_2D(self):
        img = self.image.copy()
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        hist_2d = cv.calcHist([hsv], [0, 1], None,  [180, 256], [0,180, 0, 256])

        #plt.imshow 显示颜色
        plt.subplot(2, 2, 1), plt.imshow(hist_2d, interpolation='nearest'), plt.title('hist_2d')
        plt.show()

        #cv.imshow 显示灰度
        cv.imshow('test', hist_2d)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def hist_back_inOpCV(self):
        roi = self.image
        hsv = cv.cvtColor(roi.copy(), cv.COLOR_BGR2HSV)
    


if __name__ == "__main__":
    hist = histogram_in_OpCV(cv.imread('..\\src\\BA&VT-4.jpg'))
    # hist.hist_gray()
    # hist.hist_gray_in_mat()
    # hist.hist_brg_in_mat()
    # hist.hist_use_mask()
    # hist.hist_equal()
    # hist.hist_equal_CLAHE()
    hist.hist_2D()