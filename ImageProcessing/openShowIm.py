#!/usr/bin/env python3
import numpy as np
import cv2
img = cv2.imread('Images/test.jpg', 0)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
