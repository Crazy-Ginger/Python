#!/usr/bin/env python3
import cv2
import numpy as np


def getBlock(img, width, height, blockW, blockH, channel):
    total = 0
    for x in range(blockW):
        for y in range(blockH):
            total += img[height+y, width+x, channel]
    average = round(total/(blockW*blockH))
    return average


def setBlock(value, startW, startH, blockW, blockH, channel):
    for w in range(blockW):
        for h in range(blockH):
            #has to be a global varible or else return part of an image (needs improvement)
            newimg[startH+h, startW+w, channel] = value


######Main code block #######
file = input()
blockH = 5 +1
blockW = 15 +1
img = cv2.imread(file)

height, width, channels = img.shape
print ("height:", height, "width:", width)
print ("image:", img[0,1080])
newimg = np.zeros((height, width, 3),np.uint8)

#1080x1920
#iterates through the horizontal pixels of each image
for x in range(0, width-blockW, blockW):
    #iterates through the verticel pixels of each image
    for y in range(0, height-blockH, blockH):
        #iterates through every RBG channel of the pixels
        for k in range(3):
            #first gets the average R,G or B value for the block, then uses that to set the value of the block
            setBlock(getBlock(img, x, y, blockW, blockH, k), x, y, blockW, blockH, k)


cv2.imshow('image', newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
