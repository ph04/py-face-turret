# This file is pure crap.
# I literally copied the demo from the face_recognition GitHub page which you can find here:
# https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
# This script is able to do the face tracking part and sends the commands to the Raspberry.
# For further details check out the README.
# Also this script works if your resolution is 640x480. If you have different numbers, change lines 68-69.
# Also check your rotations, if the rotation is inverted in the X or the Y axis, change those lines with/without a `180 - (...)` before the calculus.

import face_recognition
import cv2
import numpy as np
import urllib.parse
import urllib.request

url = "http://192.168.1.164:8080"

video_capture = cv2.VideoCapture(0)

obama_image = face_recognition.load_image_file("../idiota.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

known_face_encodings = [
    obama_face_encoding
]
known_face_names = [
    "Barack Obama"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        x = (left + right) // 2
        y = (top + bottom) // 2

        X = 180 - (x * 180 // 640 - 1) # Check first lines for more details, these are nothing but proportions to scale the coordinates.
        Y = y * 180 // 480 - 1 # If you didn't understand a single word, feel free to ask.

        values = {"x": f"{X:03}", "y": f"{Y:03}"}

        print(values)

        data = urllib.parse.urlencode(values)
        data = data.encode("ascii") # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            the_page = response.read() # probably useless idk
        
        font = cv2.FONT_HERSHEY_DUPLEX

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
