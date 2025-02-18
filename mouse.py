import cv2
evt=-1
def click(event,x,y,flags,params):
    global pnt
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Left mouse clicked ",": ",x," ",y)
        pnt=(x,y)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print("Right mouse clicked ",": ",x," ",y)
print("cv,starts its work.............")
cv2.namedWindow("window")
cv2.setMouseCallback("window",click)
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    if evt==1:
        style=cv2.FONT_HERSHEY_DUPLEX
        string=str(pnt)
        frame=cv2.putText(frame,string,pnt,style,1,(0,0,0),2)
    cv2.imshow("window",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()