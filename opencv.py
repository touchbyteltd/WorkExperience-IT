"""show image"""
import cv2

#load image
img = cv2.imread("girl.jpeg",cv2.IMREAD_COLOR)

#display image
cv2.imshow("Image", img )

cv2.waitKey(0)

