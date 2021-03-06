#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# canny1.py
# FLIR Camera preview
#
# Author : sosorry
# Date   : 2017/07/31
# Usage  : python canny1.py

import cv2
import time
import imutils

vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    frame = imutils.resize(frame, 320)
    cv2.imshow("flir", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    time.sleep(0.01)

vc.release()
cv2.destroyAllWindows()
