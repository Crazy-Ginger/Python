#!/usr/bin/python
import cv2

cap = cv2.VideoCapture(1)

while(True):
	ret, frame = cap.read()
	
	grey = cv2.cvtCOLOR(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('frame', grey)

	if cv2.waitkey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
