#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# flir_preview.py
# Preview from camera
#
# Author : sosorry
# Date   : 04/18/2015
# Usage  : python flir_preview.py

import cv2
import time
import imutils

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, 160)
    cv2.imshow("preview", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    time.sleep(0.01)

cap.release()
cv2.destroyAllWindows()

