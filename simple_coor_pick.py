import cv2
import numpy as np
img=np.zeros((300,300,3),np.uint8)
def click(event,x,y,flags,params):
    if event==cv2.EVENT_RBUTTONDOWN:
        print("right mouse clicked ",": ",x," ",y)
        b=frame[y,x,0]
        g=frame[y,x,1]
        r=frame[y,x,2]
        img[ : ] = [b, g, r]
        cv2.imshow("color",img)
cv2.namedWindow("window")
cv2.setMouseCallback("window",click)
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    cv2.imshow("window",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()