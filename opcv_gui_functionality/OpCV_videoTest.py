import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc('X','V','I','D')
out = cv.VideoWriter_fourcc('output.avi', fourcc, 20.0, (640,480))
while(True):
    ret, frame = cap.read()
    if ret == True:
        frame = cv.flip(frame, 0)
        out.write(frame)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame',gray)
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyWindow()
