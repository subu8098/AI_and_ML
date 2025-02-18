import cv2
print("cv,starts its work.............")
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,frame=cv2.threshold(frame,100,255,cv2.THRESH_BINARY)
    cv2.imshow("window",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()