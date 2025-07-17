"""Finds faces in feed from camera"""
import cv2

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Could not open camera")
        return()
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture frame")
            break
        
        cv2.imshow("Live webcamera feed", frame)
        
        cv2.waitKey(1) & 0xFF == ord('q')

if __name__ == "__main__":
    main()