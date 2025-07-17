"""Recognises who appears in photos"""
import Face_Recognition

known_image = Face_Recognition.load_image_file("girl.jpeg")
unknown_image = Face_Recognition.load_image_file("unknown.jpeg")

girl_encoding = Face_Recognition.face_encodings(known_image)[0]
unknown_encoding = Face_Recognition.face_encodings(unknown_image)[0]

results = Face_Recognition.compare_faces([girl_encoding],unknown_encoding)
