#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# canny3.py
# Canny edge detection WITHOUT blur
#
# Author : sosorry
# Date   : 2017/07/31
# Usage  : python canny3.py

import cv2
import time
import imutils

cv2.namedWindow('canny', cv2.WINDOW_NORMAL)
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    frame = imutils.resize(frame, 320)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    frame_v = frame_hsv[:,:,2]
    thresh = 50
    edges = cv2.Canny(frame_v,thresh,thresh*2, L2gradient=True)
    cv2.resizeWindow('canny', 320, 240)
    cv2.imshow("canny", edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    time.sleep(0.01)

vc.release()
cv2.destroyAllWindows()
