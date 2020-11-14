import cv2 as cv
import numpy as np

cnt_up = 0
cnt_down = 0

h = 480
w = 640

cap = cv.VideoCapture(0)
cap.set(3, 160)
cap.set(4, 120)

up = int(2*(h/5))
down = int(3*(h/5))

up_limit = int(1*(h/5))
down_limit = int(4*(h/5))

down_color = (255, 0, 0)
up_color = (0, 0, 255)
pt1 = [0, down]
pt2 = [w, down]
L1 = np.array([pt1, pt2], np.int32)
L1 = L1.reshape((-1, 1, 2))
pt3 =  [0, up];
pt4 =  [w, up];
L2 = np.array([pt3,pt4], np.int32)
L2 = L2.reshape((-1,1,2))

pt5 = [0, up_limit]
pt6 = [w, up_limit]
L3 = np.array([pt5,pt6], np.int32)
L3 = L3.reshape((-1,1,2))
pt7 =  [0, down_limit];
pt8 =  [w, down_limit];
L4 = np.array([pt7,pt8], np.int32)
L4 = L4.reshape((-1,1,2))

tracker = cv.TrackerCSRT_create()

ret, frame = cap.read()

cv.namedWindow('Select Window')
cv.imshow('Select Window', frame)

rect = cv.selectROI('Select Window', frame, fromCenter=False, showCrosshair=True)
cv.destroyWindow('Select Window')

font = cv.FONT_HERSHEY_SIMPLEX
tracker.init(frame, rect)

while True:
    ret, frame = cap.read()
    
    success, box = tracker.update(frame)
    
    left, top, w, h = [int(v) for v in box]

    cv.rectangle(frame, pt1=(left, top), pt2=(left + w, top + h), color=(255, 255, 255),
                 thickness=3)
    
    str_up = 'UP: '+ str(cnt_up)
    str_down = 'DOWN: '+ str(cnt_down)
    frame = cv.polylines(frame,[L1],False,down_color,thickness=2)
    frame = cv.polylines(frame,[L2],False,up_color,thickness=2)
    frame = cv.polylines(frame,[L3],False,(255,255,255),thickness=1)
    frame = cv.polylines(frame,[L4],False,(255,255,255),thickness=1)
    cv.putText(frame, str_up ,(10,40),font,0.5,(255,255,255),2,cv.LINE_AA)
    cv.putText(frame, str_up ,(10,40),font,0.5,(0,0,255),1,cv.LINE_AA)
    cv.putText(frame, str_down ,(10,90),font,0.5,(255,255,255),2,cv.LINE_AA)
    cv.putText(frame, str_down ,(10,90),font,0.5,(255,0,0),1,cv.LINE_AA)

    cv.imshow('Video', frame)
    
    k = cv.waitKey(1)
    if k == 27:
        break
        
cap.release()
cv.destroyAllWindows()