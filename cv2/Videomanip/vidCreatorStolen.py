import cv2
import argparse
import os
ap = argparse.ArgumentParser()
ap.add_argument("-ext","--extension", required=False,default='png',help="extention name. default is 'png'.")
ap.add_argument("-o","--output",required=False,default="output.mp4",help="output vidoe file")
args=vars(ap.parse_args())

dir_path='.'
ext=args['extension']
output=args['output']

images=[]
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

image_path=os.path.join(dir_path,images[0])
frame=cv2.imread(image_path)
cv2.imshow("video",frame)
height,width,channels=frame.shape

fourcc=cv2.VideoWriter_fourcc(*'mp4v')
out=cv2.VideoWriter(output, fourcc, 1, (width,height))

for image in images:
    image_path = os.path.join(dir_path,image)
    frame=cv2.imread(image_path)
    out.write(frame)
    cv2.imshow('video',frame)
    cv2.waitKey(1000)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cv2.destroyAllWindows()

print("The output video is {}". format(output))
