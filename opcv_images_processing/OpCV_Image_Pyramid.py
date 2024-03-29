import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def gaussian_pyramid_down():
    A = cv.imread("..\\src\\Rika_flower.png")
    A = cv.cvtColor(A,cv.COLOR_BGR2RGB)
    pic_list = [A]
    num = 5
    for i in range(num):
        pry_down = cv.pyrDown(pic_list[i])
        pic_list.append(pry_down)
    for i in range(num+1):
        plt.subplot(2,3,i+1), plt.imshow(pic_list[i]), plt.title("No: "+str(i))
    plt.show()

def gaussian_pyramid_up():
    B = cv.imread("..\\src\\Rika_cry.png")
    B = cv.cvtColor(B, cv.COLOR_BGR2RGB)
    pic_list = [B]
    num = 5
    for i in range(num):
        pry_down = cv.pyrDown(pic_list[i])
        pic_list.append(pry_down)
    for i in range(num + 1):
        plt.subplot(2, 3, i + 1), plt.imshow(pic_list[i]), plt.title("No: "+str(i))
    plt.show()

def laplacian_pyramid():
    img = cv.imread('..\\src\\Rika_flower.png')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    pic_list = [img]
    pic_down = [img]
    num = 5
    for i in range(num) :
        r1 = cv.pyrDown(pic_list[i])
        r2 = cv.pyrUp(r1)
        lapPry = pic_list[i] - r2

        pic_list.append(lapPry)
        pic_down.append(r1)

    for i in range(num + 1):
        plt.subplot(2, 3, i + 1), plt.imshow(pic_list[i])
    plt.show()

if __name__ == '__main__':
    gaussian_pyramid_down()
    gaussian_pyramid_up()
    laplacian_pyramid()
    pass