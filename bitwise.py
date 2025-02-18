import cv2
import numpy as np
img=np.zeros((300,300,1),np.uint8)
img[100:200,100:200]=150
img2=np.zeros((300,300,1),np.uint8)
img2[0:200,0:200]=150
img3=cv2.bitwise_xor(img,img2)
cv2.imshow("window",img)
cv2.imshow("window2",img2)
cv2.imshow("window3",img3)
while True:
    if cv2.waitKey(1)==ord('q'):
        break


cam.release()
cv2.destroyAllWindows()




""" AI Learning Journey: Bitwise Operations with OpenCV
Introduction
In this part of my AI learning journey, I explored bitwise operations using OpenCV, a powerful library for computer vision tasks. Bitwise operations are fundamental in image processing, allowing for pixel-level manipulation of images.

Program Overview
The bitwise.py program demonstrates the use of the cv2.bitwise_xor function to perform a bitwise XOR operation on two images. Here's a breakdown of the code:

import cv2
import numpy as np

# Create a black image of size 300x300 with a single channel (grayscale)
img = np.zeros((300, 300, 1), np.uint8)

# Set a square region in the image to a gray value of 150
img[100:200, 100:200] = 150

# Create another black image of the same size
img2 = np.zeros((300, 300, 1), np.uint8)

# Set a different square region in the second image to a gray value of 150
img2[0:200, 0:200] = 150

# Perform a bitwise XOR operation between the two images
img3 = cv2.bitwise_xor(img, img2)

# Display the original images and the result of the XOR operation
cv2.imshow("window", img)
cv2.imshow("window2", img2)
cv2.imshow("window3", img3)

# Wait for the 'q' key to be pressed to exit the loop and close the windows
while True:
    if cv2.waitKey(1) == ord('q'):
        break
    
    Key Learnings
Image Creation and Manipulation:

Learned how to create black images using np.zeros and manipulate specific regions by assigning pixel values.
Bitwise Operations:

Understood the concept of bitwise XOR operation, which compares corresponding pixels of two images and sets the resulting pixel to 1 if the pixels are different, and 0 if they are the same.
Displaying Images:

Practiced using cv2.imshow to display images in separate windows and cv2.waitKey to handle keyboard events for closing the windows. """