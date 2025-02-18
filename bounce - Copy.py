import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)
dw=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dh=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(dw," ",dh)
x=10
y=2
rx=2
ry=2
while True:
    ret,frame=cam.read()
    frame=cv2.rectangle(frame,(x,y),(x+15,y+10),(255,0,0),-1)
    cv2.imshow("win",frame)
    x=x+rx
    y=y+ry
    if x<=0 or x>=dw:
        rx=rx*-1
    if y<=0 or y>=dh:
        ry=ry*-1
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
