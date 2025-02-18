import cv2
print("cv,starts its work.........................")
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    frame=cv2.rectangle(frame,(0,0),(500,700),(232,156,208),3)
    frame=cv2.circle(frame,(240,250),50,(0,200,0),3)
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame,"hai subu,hurrey",(10,200),fnt,2,(10,15,100),3)
    frame=cv2.line(frame,(0,0),(600,500),(0,0,0),2)
    frame=cv2.arrowedLine(frame,(0,600),(500,0),(255,0,0),2)
    cv2.imshow('new_Window',frame)
    cv2.moveWindow('new_Window',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()