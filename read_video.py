import cv2
print("cv,starts its work.............")
cam=cv2.VideoCapture('videos/output.mp4')
# out = cv2.VideoWriter('videos/output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 21, (640, 480))
while True:
    ret,frame=cam.read()
    cv2.imshow("window",frame)
    # out.write(frame)
    if cv2.waitKey(21)==ord('q'):
        break
cam.release()
# out.release()
cv2.destroyAllWindows()


