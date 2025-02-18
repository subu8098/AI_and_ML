import cv2
print("hurrey,im start to run........")
cam=cv2.VideoCapture(0)
eye_cascade=cv2.CascadeClassifier(r"C:\Users\SUBRAMANI V\AI_python\cascade\haarcascade_eye.xml")
while True:
    rat,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    eyes=eye_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('eye Detection',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    

