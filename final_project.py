# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

import cv2
import time
import datetime

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    cv2.imshow ("Camera", frame)

    if cv2.waitKey(1) == ord('h'):
        break 

capture.release()
cv2.destroyAllWindows()