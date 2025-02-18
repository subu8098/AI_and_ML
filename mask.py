import cv2
import numpy as np
img2=np.zeros((300,300,1),np.uint8)
img2[0:200,0:200]=255
cv2.imshow("window2",img2)
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(300,300))
    cv2.imshow("frame",frame)
    img=cv2.bitwise_and(frame,frame,mask=img2)
    cv2.imshow("window",img)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
