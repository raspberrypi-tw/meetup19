#!/usr/bin/python
# -*- coding: utf-8 -*-
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

vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    rows, cols = frame.shape[:2]
    resize = cv2.resize(frame, (4*cols, 4*rows), interpolation = cv2.INTER_CUBIC)
    cv2.imshow("flir", resize)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
