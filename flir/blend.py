#!/usr/bin/python
# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# blend.py
# FLIR Camera + Raspberry Pi Camera alpha blending
#
# Author : sosorry
# Date   : 2017/07/31
# Usage  : python blend.py

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('blend', cv2.WINDOW_NORMAL)
cv2.createTrackbar('alpha', 'blend', 0, 10, nothing)

# FLIR Camera
cap1 = cv2.VideoCapture(0)
cap1.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  320)
cap1.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

# Raspberry Pi Camera
cap2 = cv2.VideoCapture(1)
cap2.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  320)
cap2.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
#cap2.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  640)
#cap2.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

while True:
    alpha = cv2.getTrackbarPos('alpha', 'blend')
    ret, img1 = cap1.read()
    ret, img2 = cap2.read()

    rows, cols = img1.shape[:2]
    resize = cv2.resize(img1, (4*cols, 4*rows), interpolation = cv2.INTER_CUBIC)
    #resize = cv2.resize(img1, (8*cols, 8*rows), interpolation = cv2.INTER_CUBIC)    # 640x480

    cv2.resizeWindow('blend', 320, 240)
    #cv2.resizeWindow('blend', 640, 480)    # 640x480
    cam_alpha = float(alpha)/10
    flir_alpha = float(10-alpha)/10
    dst = cv2.addWeighted(img2, cam_alpha, resize, flir_alpha, 0)
    cv2.imshow("blend", dst)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

