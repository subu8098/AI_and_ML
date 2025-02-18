import cv2
print("hurrey,im start to run........")
cam=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(r"C:\Users\SUBRAMANI V\AI_python\cascade\face.xml")
while True:
    rat,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Face Detection',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    

