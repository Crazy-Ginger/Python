import cv2
import os
file = input()
#create capture and video to read from and to write to
cap = cv2.VideoCapture(file+".MOV")
fourcc= cv2.VideoWriter_fourcc(*'mp4v')
Video=cv2.VideoWriter("Video",fourcc,10,(1080,1920))
cVideo= cv2.VideoWriter("cVideo",fourcc,10,(1080,1920))
success,frame = cap.read()
count = 0
success = True
while (cap.isOpened()):
    success,frame=cap.read()
    if success == True :
        #cv2.imshow("frame",frame)
        Video.write(frame)
        cFrame= cv2.Canny(frame,10,100)
        cVideo.write(cFrame)
        cv2.imshow("cFrame",cFrame)
        if cv2.waitKey(25)&0xFF==ord('q'):
            break
    else:
        break
Video.release()
cVideo.release()
cv2.destroyAllWindows()
