"""Recognises faces"""
import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


known_faces_files = ["me2.jpg", "girl.jpeg", "girl2.jpeg"]
known_labels = ["Me", "Girl", "Girl2"]

known_faces = []

for file in known_faces_files:
    img = cv2.imread(file)
    if img is None:
        print(f"Could not load image {file}")
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    if len(faces) == 0:
        print("No face found in image")
        continue

(x, y, w, h) = faces[0]
face_roi = gray[y:y+h, x:x+w]
face_resized= cv2.resize(face_roi, (100, 100))
known_faces.append(face_resized)


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

        label = "Unknown"
        colour = (0, 0, 255)
        threshold = 70000

        for i, known_face in enumerate(known_faces):
            diff = cv2.absdiff(known_face, face_resized)
            score = np.sum(diff)
            

            if score < threshold:
                label = known_faces_fileslabels[i]
                colour (0, 255, 0)
                break

        cv2.rectangle(frame, (x, y), (x+w, y+h), colour, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colour, 2)

    cv2.imshow("Webcamera - Multiple Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cap.destroyAllWindows()