import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((1000,1000,3),np.uint8)

#a line from (0,0) to (200,200) of 5 thick and a colour set by (255, 200, 50)
cv2.line(img, (0,0), (200, 200), (-100, -2, -27), 5)

#a rectangle from (300, 200) to (400, 500) with a thickness of 3 to fill it in set thick to -1
cv2.rectangle(img, (300, 200), (400, 500), (0, 130, 20), 3)

#a circle with a midpoint at (447, 63) and a radius of 40
cv2.circle(img, (447, 63), 40, (0, 10, 100), -1)


#an ellipse with a centre (500, 500) that is 100 wide and 400 tall
#37 is the angle offset of the ellipse
#90 and 270 set how much of the elipse is being drawn (0 & 360 for a full elipse)
cv2.ellipse(img, (500, 500), (100, 400), 37, 90, 270, (255, 255, 255), -1)
    
#a unfilled polygon first a new array of the verticies needs to be created
#then this needs to be converted so cv2 can use it (don't know how this works)
#True refers to whether the shape will be completed
pts = np.array([[100, 50], [700, 200], [200,710]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts],True,(30,203,109))

#a filled polygon
pts = np.array([[100, 50], [700, 200], [200,710]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(img, [pts], (30,203,109))


cv2.imshow("image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

