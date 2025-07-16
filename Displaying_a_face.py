""""Displays feed from camera"""
import cv2

# Opens USB camera
cap = cv2.VideoCapture(0)

# Checks if the camera has opened successfully
if not cap.isOpened():
    print("Could not open camera")
    exit()

# Reads a single frame
ret, frame = cap.read()

# Shows the image if the frame is corrrectly read
if ret:
    cv2.imshow("captured Frame", frame)
    cv2.waitKey(0)
else:
    print("Could not read frame")