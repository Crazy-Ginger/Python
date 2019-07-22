import cv2
import numpy as np
import os
import random
import datetime

#creates a np array of random length and adds random coordinates
def randArray(x, y):
    pts = np.array([(random.randint(0, x)), (random.randint(0,y))], np.int32)
    for i in range (1, random.randint(3,100)):
        np.append(pts, [(random.randint(0, x)), (random.randint(0, y))])
    pts = pts.reshape((-1, 1, 2))
    return pts


rootdir = "C:/Users/matty/Pictures/Camera Roll/Coding/Random Images using Shapes/"
os.chdir(rootdir)
x = int(input("Canvas width: "))
y = int(input("Canvas heigth: "))
area = x*y
img = np.zeros((x, y, 3),np.uint8)
fileName = str(x)+ "x" + str(y) +" " +str(datetime.datetime.now().strftime("%Y-%m-%d"))
print(fileName)

for i in range (1, random.randint(100, 1000)):
    shape = random.randint(1, 5)

    if shape == 1:
        #creates line
        cv2.line(img, (random.randint(0, x),random.randint(0, y)), (random.randint(0, x),random.randint(0, y)), (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)), random.randint(1, 20))
    elif shape == 2:
        #creates rectangle
        cv2.rectangle(img,(random.randint(0, x),random.randint(0, y)), (random.randint(0, x),random.randint(0, y)), (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)), random.randint(-1, 20))
    elif shape == 3:
        #creates circle
        cv2.circle(img, (random.randint(0, x),random.randint(0, y)), (random.randint(1, x/2)), (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)), random.randint(-1, 20))
    elif shape == 4:
        #creates an ellipse
        cv2.ellipse(img, (random.randint(0, x),random.randint(0, y)), (random.randint(1, x), random.randint(1, y)), random.randint(0, 90), random.randint(1, 360), random.randint(1, 360), (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)), random.randint(-1, 20))
    elif shape == 5:
        #creates a polygon (randomly filled or unfilled)
        boo_Filled = bool(random.getrandbits(1))
        #creates a filled polygon
        if boo_Filled == True:
            cv2.fillPoly(img, randArray(x, y), (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)))
        #creates an empty polygon
        else:
            cv2.polylines(img, randArray(x, y), boo_Filled, (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)), random.randint(1, 20))

    else:
        cont = input("Problem, continue? ")


cv2.imwrite(fileName+ ".png", img)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cannied = cv2.Canny(img, 50, 150)


cv2.imwrite(fileName + "_cannied.png", cannied)
cv2.imshow("img", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
