import cv2 as cv
import numpy as np


def nothing(x):
    pass

draw = False
ix , iy = -1, -1
def Print(event, x, y, flags, param):
    global draw, ix, iy
    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if draw == True :
            cv.circle(img, (x,y), Radius, (0,255,255),1)
    elif event == cv.EVENT_LBUTTONUP:
        draw = False


if __name__ == '__main__':
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('print')
    cv.createTrackbar('radius', 'print', 1,10, nothing)
    cv.setMouseCallback('print',Print)
    while(True):
        cv.imshow('print',img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        Radius = cv.getTrackbarPos('radius','print')
    cv.destroyAllWindows()