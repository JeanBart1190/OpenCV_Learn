import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def draw_contours():
    img = cv.imread('..\\src\\Perspective_Transform_test.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    print(contours, hierarchy)

    # cnt = contours[4]
    border = cv.drawContours(img, contours, -1, (0, 0, 255), 2)

    plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(border, cv.COLOR_BGR2RGB))
    plt.subplot(2, 2, 2), plt.imshow(cv.cvtColor(img_gray, cv.COLOR_BGR2RGB))
    plt.show()


def contour_features():
    img = cv.imread('..\\src\\Turtle_surprise.png')
    img_gray = cv.imread('..\\src\\Turtle_surprise.png', 0)

    img = cv.cvtColor(img, cv.COLOR_BGRA2RGBA)

    # img_gray = cv.cvtColor(img_gray,cv.COLOR_BGRA2RGBA)
    ret, thresh = cv.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, 1, 2)
    cnt = contours[4]
    M = cv.moments(cnt)
    print(M)

    ##求出质心的坐标
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    print(cx, cy)

    # show_mass = cv.circle(img, center=(cx,cy), radius=10, color=(255,0,255), thickness=10)
    # plt.subplot(2,2,1), plt.imshow(img), plt.title('Origianl')
    # plt.subplot(2,2,2), plt.imshow(show_mass), plt.title('Show mass')
    # plt.show()

    # 轮廓面积
    area = cv.contourArea(cnt)
    print(area)

    # 轮廓周长
    perimeter = cv.arcLength(cnt, True)
    print(perimeter)


def boundary_rectangle():
    img = cv.imread('..\\src\\Morphological_test.png')
    img_gray = cv.cvtColor(cv.cvtColor(img, cv.COLOR_BGR2RGB), cv.COLOR_RGB2GRAY)
    ret, thresh = cv.threshold(img_gray, 150, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # 直角矩形
    cnt = contours[0]
    x, y, w, h = cv.boundingRect(cnt)
    # canvas = np.zeros(img_gray.shape, dtype=np.uint8)
    canvas1 = img.copy()
    cv.rectangle(canvas1, (x, y), (x + w, y + h), (255, 0, 255), 2)

    # 旋转矩形(外接矩形?)
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.intp(box)
    canvas2 = img.copy()
    cv.drawContours(canvas1, [box], 0, (255, 255, 0), 2)

    # 绘制轮廓
    border = cv.drawContours(img, contours, 0, (0, 0, 255), 2)

    plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(thresh.copy(), cv.COLOR_BGR2RGB)), plt.title('Binarization')
    plt.subplot(2, 2, 2), plt.imshow(cv.cvtColor(border.copy(), cv.COLOR_BGR2RGB)), plt.title('border')
    plt.subplot(2, 2, 3), plt.imshow(cv.cvtColor(canvas1.copy(), cv.COLOR_BGR2RGB)), plt.title('rectangle')
    plt.show()


def boundary_circle():
    img = cv.imread('..\\src\\Morphological_test.png')
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img_gray, 150, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    # 外接圆
    (x, y), radius = cv.minEnclosingCircle(cnt)
    center, radius = (int(x), int(y)), int(radius)
    canvas1 = img.copy()
    cv.circle(canvas1, center=center, radius=radius, color=(0, 0, 255), thickness=2)

    # 拟合椭圆
    ellipse = cv.fitEllipse(cnt)
    cv.ellipse(canvas1, ellipse, (0, 255, 0), 2)

    # 绘制轮廓
    border = cv.drawContours(img, contours, 0, (0, 0, 255), 2)

    plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('origianl')
    plt.subplot(2, 2, 2), plt.imshow(cv.cvtColor(border, cv.COLOR_BGR2RGB)), plt.title('border')
    plt.subplot(2, 2, 3), plt.imshow(cv.cvtColor(canvas1, cv.COLOR_BGR2RGB)), plt.title('circle&ellipse')

    plt.show()


def fit_line():
    img = cv.imread('..\\src\\Morphological_test.png')
    img_gray = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img_gray, 150, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    rows, cols = img.shape[:2]
    [vx, vy, x, y] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)

    canvas1 = img.copy()
    cv.line(canvas1, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

    plt.subplot(2, 2, 1), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('origianl')
    plt.subplot(2, 2, 2), plt.imshow(cv.cvtColor(canvas1, cv.COLOR_BGR2RGB)), plt.title('border')

    plt.show()

def outline_properties():
    img = cv.imread('..\\src\\Morphological_test.png')
    img_gray = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img_gray, 150, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    #长宽比
    x, y, w, h = cv.boundingRect(cnt)
    aspect_ratio = float(w)/h
    print(aspect_ratio)

    #范围
    area = cv.contourArea(cnt)
    x, y, w, h = cv.boundingRect(cnt)
    rect_area = w*h
    extent = float(area)/rect_area
    print(extent)

    #固实性--轮廓面积与其凸包面积的比率。
    area = cv.contourArea(cnt)
    hull = cv.convexHull(cnt)
    hull_area = cv.contourArea(hull)
    solidity = float(area) / hull_area
    print(solidity)

    #等效直径--面积与轮廓面积相同的圆的直径
    area = cv.contourArea(cnt)
    equi_diameter = np.sqrt(4*area/np.pi)
    print(equi_diameter)

    #方向--物体指向的角度
    (x, y), (MA, ma), angle = cv.fitEllipse(cnt)
    print((x,y), (MA, ma), angle)

    #平均颜色或平均强度
    mask = np.zeros(img_gray.shape, np.uint8)
    mean_val = cv.mean(img, mask=mask)
    print(mean_val)

    #极端点
    leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
    bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])

    cv.circle(img, leftmost, 5, (0,0,255), -1)
    cv.circle(img, rightmost, 5, (0,0,255), -1)
    cv.circle(img, topmost, 5, (0,0,255), -1)
    cv.circle(img, bottommost, 5, (0,0,255), -1)

    cv.imshow('Points', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    # contour_features()
    boundary_rectangle()
    boundary_circle()
    fit_line()
    outline_properties()
    pass
