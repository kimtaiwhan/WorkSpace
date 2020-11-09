import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1080)

tracker = cv2.TrackerCSRT_create()

ret, frame = cap.read()

cv2.namedWindow('Select Window')
cv2.imshow('Select Window', frame)

rect = cv2.selectROI('Select Window', frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow('Select Window')

tracker.init(frame, rect)

while True:
    ret, frame = cap.read()
    
    success, box = tracker.update(frame)
    
    left, top, w, h = [int(v) for v in box]

    cv2.rectangle(frame, pt1=(left, top), pt2=(left + w, top + h), color=(255, 255, 255),
                 thickness=3)
    
    cv2.imshow('Video', frame)
    
    k = cv2.waitKey(1)
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()