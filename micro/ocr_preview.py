#!/usr/bin/python
# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ocr_preview.py
# Do OCR in fixed area.
#
# Author : sosorry
# Date   : 2017/07/31
# Usage  : python ocr_preview.py CAMERA_ID
# Example: python ocr_preview.py 0

import cv2
import numpy as np
import pytesseract
from PIL import Image
import sys


camera_id = sys.argv[1]
cap = cv2.VideoCapture( int(camera_id) )
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  320)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

src_file = "ocr.png"
asciidata = None

while True:
    ret, frame = cap.read()

    if asciidata is not None:
        cv2.rectangle(frame, (10, 190), (200, 230), (255, 255, 255), thickness=cv2.cv.CV_FILLED)
        cv2.putText(frame, asciidata, (10, 220), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=2)

    offset = 15
    x, y = 100, 50
    w, h = 230, 70
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    img = frame[y:y+h, x:x+w]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=3)
    img = cv2.erode(img, kernel, iterations=3)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 1)
    shift_img = img[offset:h+offset, offset:w+offset]
    cv2.imshow("preview", frame)
    cv2.imshow("ocr", shift_img)

    if cv2.waitKey(1) & 0xFF == ord("t"):
        cv2.imwrite("thres.png", shift_img)
        print '--- Start recognize text from image ---'
        data = pytesseract.image_to_string(Image.open("thres.png"))
        print data
        asciidata = data.encode("ascii","ignore")
        print "------ Done -------"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

