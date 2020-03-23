#!/usr/bin/env python3

import numpy as np
import cv2 as cv

img = cv.imread('Images/circles.jpg')
#img = cv.medianBlur(img, 5) #when added it breaks the code somehow
gimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(gimg, cv.HOUGH_GRADIENT, 1, 20, param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    #draw the outer circle
    cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the center of the circle
    #cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',img)
cv.waitKey(0)
cv.destroyAllWindows()
