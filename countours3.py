#it will track all the color in range
import  cv2
import numpy as np
print("cv2,starts its work............................")
cam=cv2.VideoCapture(0)
cv2.namedWindow("trackbar")
cv2.createTrackbar('Hl','trackbar',40,179,lambda x:None)
cv2.createTrackbar('Hh','trackbar',100,179,lambda x:None)
cv2.createTrackbar('Hl2','trackbar',50,179,lambda x:None)
cv2.createTrackbar('Hh2','trackbar',150,179,lambda x:None)
cv2.createTrackbar('Sl','trackbar',50,255,lambda x:None)
cv2.createTrackbar('Sh','trackbar',255,255,lambda x:None)
cv2.createTrackbar('Vl','trackbar',50,255,lambda x:None)
cv2.createTrackbar('Vh','trackbar',255,255,lambda x:None)
cv2.moveWindow("trackbar",900,0)
while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(300,300))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    Hl=cv2.getTrackbarPos('Hl','trackbar')
    Hh=cv2.getTrackbarPos('Hh','trackbar')
    Hl2=cv2.getTrackbarPos('Hl2','trackbar')
    Hh2=cv2.getTrackbarPos('Hh2','trackbar')
    Sl=cv2.getTrackbarPos('Sl','trackbar')
    Sh=cv2.getTrackbarPos('Sh','trackbar')
    Vl=cv2.getTrackbarPos('Vl','trackbar')
    Vh=cv2.getTrackbarPos('Vh','trackbar')

    L_range=np.array([Hl,Sl,Vl])
    H_range=np.array([Hh,Sh,Vh])

    L_range2=np.array([Hl2,Sl,Vl])
    H_range2=np.array([Hh2,Sh,Vh])

    FG_mask=cv2.inRange(hsv,L_range,H_range)

    FG_mask2=cv2.inRange(hsv,L_range2,H_range2)

    FG_comp=cv2.add(FG_mask,FG_mask2)
    cv2.imshow("FG_comp",FG_comp)
    contours,_=cv2.findContours(FG_comp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for i in contours:
        x,y,w,h=cv2.boundingRect(i)
        if cv2.contourArea(i)>100:
           cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3) 
    
    cv2.imshow('frame',frame)
    cv2.moveWindow('frame',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
