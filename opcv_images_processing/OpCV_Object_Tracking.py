import cv2 as cv
import numpy as np

def Object_Tracking():
    cap = cv.VideoCapture(0)
    while(True):
        _, frame = cap.read()

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        lowerRed = np.array([110,100,100])
        upperRed = np.array([130,255,255])

        lowerBlue = np.array([110,50,50])
        upperBlue = np.array([130,255,255])

        lowerGreen = np.array([50,100,100])
        upperGreen = np.array([70,255,255])

        maskRed = cv.inRange(hsv, lowerRed, upperRed)
        maskBlue = cv.inRange(hsv, lowerBlue, upperBlue)
        maskGreen = cv.inRange(hsv, lowerGreen, upperGreen)

        finalmask = cv.bitwise_or(maskRed, maskBlue)
        finalmask = cv.bitwise_or(finalmask, maskGreen)

        res = cv.bitwise_and(frame, frame, mask=finalmask)
        cv.imshow('frame', frame)
        cv.imshow('mask', finalmask)
        cv.imshow('res', res)
        k = cv.waitKey(10) & 0xFF
        if k == 27 :
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    Object_Tracking()

