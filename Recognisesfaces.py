"""Recognises faces"""
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

known_img = cv2.imread("Girl2.jpg")
known_gray = cv2.cvtColor(known_img, cv2.COLOR_BGR2GRAY)

known_faces = face_cascade.detectMultiScale(known_gray, 1.1, 5)

if len(known_faces) == 0:
    print("No face found in image")
    exit()

(x, y, w, h) = known_faces[0]
known_face = known_gray[y:y+h, x:x+h]
known_face = cv2.resize(known_face, (100,100))

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Could not open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face_roi, (100,100))

        diff = cv2.absdiff(face_resized, known_face)
        score = np.sum(diff)
        threshold = 100000

        if score < threshold:
            label = "Matched"
            colour = (0, 255, 0)

        else:
            label = "Unknown"
            colour = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), colour, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colour, 2)

    cv2.imshow("Webcamera - Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cap.destroyAllWindows()