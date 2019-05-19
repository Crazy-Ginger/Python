#!/usr/bin/env python3
import numpy as np
import argparse
import cv2
import time

cap = cv2.VideoCapture(0) 

while(True):
    ret, frame = cap.read()

    output = frame.copy()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.blur(grey, (2, 3))

    circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 1.1, 70, param1=70, param2=100, minRadius=0, maxRadius=0)

    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)

    # Display the resulting frame
    cv2.imshow('frame',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
