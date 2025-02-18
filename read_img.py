import cv2


img = cv2.imread(r"C:\Users\SUBRAMANI V\Pictures\WhatsApp Image 2024-12-31 at 10.23.12_e6961b64.jpg")
cv2.imshow("window", img)
while True:
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()