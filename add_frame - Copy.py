import cv2
import numpy as np
img2=np.zeros((300,300,1),np.uint8)
img2[0:200,0:200]=255
cv2.imshow("window2",img2)
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(300,300))
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blended=cv2.addWeighted(frame,0.7,img2,0.3,0)
    cv2.imshow("blended",blended)
    cv2.moveWindow("blended",400,0)
    cv2.imshow("frame",frame)
    img=cv2.add(frame,img2)
    cv2.imshow("window",img)
    cv2.moveWindow("window",0,340)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
