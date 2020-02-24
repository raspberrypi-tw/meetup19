#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#

import cv2
import time
import imutils

#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)
#cap.set(PROP_FRAME_WIDTH, 80)
#cap.set(PROP_FRAME_HEIGHT, 60)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, 320)
    cv2.imshow("preview", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    time.sleep(0.01)

cap.release()
cv2.destroyAllWindows()

