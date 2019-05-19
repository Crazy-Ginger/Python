#import os
from PIL import Image, ImageFilter
import cv2
#os.chdir("C:\\Users\matty\Pictures")
img = Image.open("test.jpg")
#im.show()
im_sharp = im.filter(ImageFilter.SHARPEN)
im_sharp.save("image_sharp.jpg", "JPEG")
sharp = Image.open("image_sharp.jpg")
sharp.show()
r,g,b = im_sharp.split()
r.show()
g.show()
b.show()
exif_data = im._getexif()
exif_data
