"""Detects faces through USB webcamera"""
import cv2
# loads the pre-trained Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

# checks if camera has opened
if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:

    # reads frames from the webcamera
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break
    
    # converst to gray scale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detects faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # draws rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # displays the frames
    cv2.imshow("Webcamera - Detected faces", frame)

    if cv2.waitKey(1) & 0xFF == ord ("q"):
        cap.release()
        cv2.destroyAllWindows()