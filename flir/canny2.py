#!/usr/bin/python
# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# canny2.py
# FLIR image to Gray scale image preview
#
# Author : sosorry
# Date   : 2017/07/31
# Usage  : python canny2.py

import cv2

vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    frame_v = frame_hsv[:,:,2]
    rows, cols = frame_v.shape[:2]
    resize = cv2.resize(frame_v, (4*cols, 4*rows), interpolation = cv2.INTER_CUBIC)
    cv2.imshow("gray", resize)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
