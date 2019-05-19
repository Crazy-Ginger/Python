#!/usr/bin/env python3
import cv2

cap = cv2.VideoCapture(1)
fgbg =  cv2.createBackgroundSubtractorKNN()
while(True):
    ret, frame = cap.read()
    
    #grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask =  fgbg.apply(frame)
    
    cv2.imshow('frame', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
