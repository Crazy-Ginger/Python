import cv2
import numpy as np
from matplotlib import pyplot as plt
#using os to select images from Pictures folder in windows should be changed for when using in linux
import os
os.chdir("C:\\Users\matty\Pictures\Saved Pictures")

img = cv2.imread('Random Steam #2.jpg',0)
edges = cv2.Canny(img,100,200)

#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
