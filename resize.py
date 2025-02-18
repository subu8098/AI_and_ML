import cv2
print("hurrey,im start to run........")
cam=cv2.VideoCapture(0)
while True:
    rat,frame=cam.read()
    cv2.imshow('window1',frame)
    cv2.moveWindow('window1',0,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2LUV)
    graySmall=cv2.resize(gray,(320,260))
    cv2.imshow('window2',graySmall)
    cv2.moveWindow('window2',950,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    

