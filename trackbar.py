import cv2
def dummy(x):
    pass
cv2.namedWindow("window")
cv2.createTrackbar("x","window",10,600,dummy)
cv2.createTrackbar("y","window",10,400,dummy)
cv2.createTrackbar("w","window",100,600,dummy)
cv2.createTrackbar("h","window",100,400,dummy)
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    x=cv2.getTrackbarPos("x","window")
    y=cv2.getTrackbarPos("y","window")
    w=cv2.getTrackbarPos("w","window") 
    h=cv2.getTrackbarPos("h","window")  
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("window",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()