"""Finds a face in an image"""
import cv2

# loads image
img = cv2.imread("partialside.jpeg")

# converts to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# loads Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# detects the faces with positional arguments
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# puts a rectangle around face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("detected faces", img)
cv2.waitKey(0)
