import numpy as np
import cv2
import os

rootdir = "C:/Users/matty/Pictures/Camera Roll/Coding/"
os.chdir(rootdir)


vid = cv2.VideoCapture('Test 1.mp4')

fgbg = cv2.createBackgroundSubtractorKNN()

while(1):
    ret, frame = vid.read()

    fgmask = fgbg.apply(frame)
    #fgmask = cv2.Canny(fgmask, 150,300)
    
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(10) & 0xff
    if k==27:
        break
vid.release()
cv2.destroyAllWindows()
