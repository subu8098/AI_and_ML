import cv2
print("cv,starts its work.............")
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    newframe=frame[100:300,250:400].copy()
    frame[100:300,250:400]=[255,255,255]
    cv2.imshow("window",frame)
    cv2.imshow("win2",newframe)
    cv2.moveWindow("window",0,0)
    cv2.moveWindow("win2",600,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()