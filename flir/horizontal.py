#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import cv2
import numpy as np
import time
import imutils

# FLIR Camera
flr = cv2.VideoCapture(1)

# Raspberry Pi Camera
cam = cv2.VideoCapture(0)

while True:
    ret, img1 = flr.read()
    ret, img2 = cam.read()

    img1 = imutils.resize(img1, 320)
    img2 = imutils.resize(img2, 320)

    horizontal = np.hstack((img1, img2))

    cv2.imshow('horizontal', horizontal)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    time.sleep(0.01)

flr.release()
cam.release()
cv2.destroyAllWindows()

