import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# print (events)

# def drawCircle(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN :
#         cv.circle(img, (x,y), 20, (255,0,0,255), 1)
#
# img = np.zeros((512,512,4), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image', drawCircle)
# while(True):
#     cv.imshow('image', img)
#     if cv.waitKey(20) & 0xFF == 27 :
#         break
# cv.destroyAllWindows()

drawing = False
mode = True
ix, iy = -1, -1
def drawShape(event, x ,y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x ,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x,y), (0,255,0,255), 1 )
            else:
                cv.circle(img, (x,y), 5, (0,0,255,255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix,iy), (x,y), (0,255,0,255), 1)
        else:
            cv.circle(img, (x,y), 10, (0,0,255,255), )

img = np.zeros((512,512,4), np.uint8)
cv.namedWindow('Test')
cv.setMouseCallback('Test',drawShape)
while(True):
    cv.imshow('Test', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m') :
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()

# drawing = False # 如果 True 是鼠标按下
# mode = True # 如果 True，画矩形，按下‘m’切换到曲线
# ix,iy = -1,-1
# # 鼠标回调函数
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
#                 cv.circle(img,(x,y),5,(0,0,255),-1)
#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         else:
#             cv.circle(img,(x,y),5,(0,0,255),-1)
#
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)
# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
# cv.destroyAllWindows()

