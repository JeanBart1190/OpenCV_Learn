import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class HoughTransform:
    def __init__(self):
        self.image = cv.imread("..\\src\\sudoku.jpg")
        self.image_gray = cv.cvtColor(self.image.copy(), cv.COLOR_BGR2GRAY)

    def hough_line(self):
        img = self.image.copy()
        img_gray = self.image_gray.copy()

        edges = cv.Canny(img_gray, 180, 200)
        lines = cv.HoughLines(edges, 1, np.pi / 360, 180)

        for line in lines:
            rho, theta = line[0]

            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a * rho
            y0 = b * rho

            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv.line(img, (x1, y1), (x2, y2), (0, 255, 0))

        plt.figure(figsize=(8, 4), dpi=180)
        plt.subplot(2, 2, 1), plt.imshow(img[:, :, ::-1]), plt.title("hough line detect")
        plt.subplot(2, 2, 2), plt.imshow(edges,'gray'), plt.title('edges')
        plt.xticks([]), plt.yticks([])
        plt.show()

    def hough_circle(self, src):
        img = cv.imread(src)
        img_gray = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)

        # 圆检测对噪声敏感, 中值滤波降噪
        img_gray = cv.medianBlur(img_gray, 5)
        circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 50, param1=200, param2=20, minRadius=5,
                                  maxRadius=100)
        circles = np.uint16(np.around(circles))
        print(circles[0, :])
        for i in circles[0, :]:
            # draw the outer circle
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        plt.figure(figsize=(8, 4), dpi=180)

        plt.subplot(2, 2, 1), plt.imshow(img[:, :, ::-1]), plt.title('hough circle detect')
        plt.subplot(2, 2, 2), plt.imshow(img_gray,'gray'), plt.title('gray')
        plt.xticks([]), plt.yticks([])
        plt.show()

if __name__ == '__main__':
    houghTransform = HoughTransform()
    houghTransform.hough_line()
    houghTransform.hough_circle('..\\src\\Planet.jpg')
