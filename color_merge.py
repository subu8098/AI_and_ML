import cv2
import numpy as np
blank=np.zeros((300,300,1),np.uint8)
print("cv,starts its work.............")
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(300,300))
    blue,green,red=cv2.split(frame)
    b=cv2.merge((cv2.split(frame)[0],blank,blank))
    b=cv2.resize(b,(400,400))
    g=cv2.merge((blank,cv2.split(frame)[1],blank))
    g=cv2.resize(g,(400,400))
    r=cv2.merge((blank,blank,cv2.split(frame)[2]))
    r=cv2.resize(r,(400,400))
    cv2.imshow("blue",b)
    cv2.imshow("green",g)
    cv2.imshow("red",r)
    cv2.imshow("window",frame)
    cv2.moveWindow("window",0,0)
    cv2.moveWindow("blue",400,0)
    cv2.moveWindow("green",0,400)
    cv2.moveWindow("red",400,400)
    mergedWindow=cv2.merge((blue,green,red))
    cv2.imshow("merged",mergedWindow)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

