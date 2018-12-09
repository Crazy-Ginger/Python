import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
os.chdir("C:\\Users\matty\Pictures\Saved Pictures")

img = cv2.imread('People #1.jpg',0)
img = cv2.resize(img,(1920,1080))
cv2.imshow("Image",img)
x,y = 1,1
#for i in range(100):
edges = cv2.Canny(img,100,400)
#plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
    
x += 1
    #y+=2
plt.show()
