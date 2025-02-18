import cv2
import numpy as np
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
print("cv2,starts its work")
while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(300,300))
    cv2.imshow("image",frame)
    cv2.moveWindow("image",0,0)


    Hl=cv2.getTrackbarPos('Hl','trackbar')
    Hh=cv2.getTrackbarPos('Hh','trackbar')
    Hl2=cv2.getTrackbarPos('Hl2','trackbar')
    Hh2=cv2.getTrackbarPos('Hh2','trackbar')

    Sl=cv2.getTrackbarPos('Sl','trackbar')
    Sh=cv2.getTrackbarPos('Sh','trackbar')
    Vl=cv2.getTrackbarPos('Vl','trackbar')
    Vh=cv2.getTrackbarPos('Vh','trackbar')
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    L_range=np.array([Hl,Sl,Vl])
    H_range=np.array([Hh,Sh,Vh])
    L_range2=np.array([Hl2,Sl,Vl])
    H_range2=np.array([Hh2,Sh,Vh])

    FG_mask=cv2.inRange(hsv,L_range,H_range)
    FG_mask2=cv2.inRange(hsv,L_range2,H_range2)
    FG_comp=cv2.add(FG_mask,FG_mask2)
    cv2.imshow("FG_comp",FG_comp)
    cv2.moveWindow("FG_comp",450,0)

    FG=cv2.bitwise_and(frame,frame,mask=FG_comp)
    cv2.imshow("FG",FG)
    cv2.moveWindow("FG",0,340)

    BG_mask=cv2.bitwise_not(FG_comp)
    cv2.imshow("BG_mask",BG_mask)
    cv2.moveWindow("BG_mask",450,340)

    # BG_mask=cv2.cvtColor(BG_mask,cv2.COLOR_GRAY2BGR)
    # BG=cv2.bitwise_and(BG,FG_mask)
    # cv2.imshow("BG",BG)

    # BG=cv2.bitwise_and(frame,BG_mask)
    # cv2.imshow("BG",BG)
    BG=cv2.cvtColor(BG_mask,cv2.COLOR_GRAY2BGR)
    BG=cv2.add(FG,BG)
    cv2.imshow("BG",BG)


    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()