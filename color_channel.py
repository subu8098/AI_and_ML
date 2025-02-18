import cv2
print("cv,starts its work.............")
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    b=cv2.split(frame)[0]
    g=cv2.split(frame)[1]
    r=cv2.split(frame)[2]
    cv2.imshow("blue",b)
    cv2.imshow("green",g)
    cv2.imshow("red",r)
    cv2.imshow("window",frame)
    cv2.moveWindow("window",0,0)
    cv2.resizeWindow("window",400,400)
    cv2.moveWindow("blue",400,0)
    cv2.resizeWindow("blue",400,400)
    cv2.moveWindow("green",0,400)
    cv2.resizeWindow("green",400,400)
    cv2.moveWindow("red",400,400)
    cv2.resizeWindow("red",400,400)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()