#!/usr/bin/env python3
import cv2
import numpy as np
#import os

#os.chdir("C:\\Users\matty\Pictures\Camera Roll\Coding")
img =  cv2.imread("Images/circles.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts the image to greyscale
cv2.imshow("Original Image",img)
cv2.waitKey(2000) #wait time in seconds, if 0 the window will stay open for ever
cv2.destroyAllWindows()

cv2.imshow("Grey Image",grey_img)
cv2.waitKey(2000)
cv2.destroyAllWindows() #destroy the windows it created

#cv2.imwrite("greyimage.jpg",grey_img) #saves the image
