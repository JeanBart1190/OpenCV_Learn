import cv2 as cv
import numpy as np
import os

img = np.zeros((512,512,4), np.uint8)
#画直线
cv.line(img, pt1 = (0,0), pt2 = (511,511), color=(255,0,0,255), thickness=5, lineType=cv.LINE_AA)
#画圆形
cv.circle(img,center = (447,63), radius=63, color = (0,0,255, 120), thickness=-1)
#画矩形
cv.rectangle(img, pt1=(384,0), pt2=(510,128), color = (0,255,0,255), thickness=3)
#画椭圆
cv.ellipse(img, (256,256), (100,50),0, 0, 180, color = (127,127,127,255), thickness=-1)
#画多边形
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img, [pts], True, (0,255,255,255))

#写字
cv.putText(img, 'OpenCV', (25, 450), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 2, cv.LINE_AA)
cv.imwrite('..\\OutputFiles\\image.png', img)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyWindow()