import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    cv2.imshow("subu",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
