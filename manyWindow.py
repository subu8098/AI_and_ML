import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:
    rat,frame=cam.read()
    cv2.imshow('window1',frame)
    cv2.moveWindow('window1',0,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2LUV)
    cv2.imshow('window2',gray)
    cv2.moveWindow('window2',640,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    

