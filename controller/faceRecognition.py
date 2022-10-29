import face_recognition
import cv2
import numpy as np
import os
import glob
faces_encodings = []
faces_names = []
cur_direc = os.getcwd()
path = os.path.join(cur_direc + '\\data\\faces\\')
print(path)

# list_of_files = []
# #for f in glob.glob(path+'*.jpg'):
# #    list_of_files.append(f)

list_of_files = [f for f in glob.glob(path+'*.jpeg')]
print(list_of_files)

number_files = len(list_of_files)
names = list_of_files.copy()
for i in range(number_files):
    presets = face_recognition.load_image_file(list_of_files[i])
    encoding = face_recognition.face_encodings(presets)[0]
    faces_encodings.append(encoding)
    nome = names[i].replace(cur_direc+"\\faces\\", "")
    nome = nome.replace(".jpg", "")
    names[i] = nome
    faces_names.append(names[i])

print("Face Names", faces_names)
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:

    ret, frame = video_capture.read()
    rgb_small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                faces_encodings, face_encoding)
            print(matches)

            name = "Desconhecido"
            face_distances = face_recognition.face_distance(
                faces_encodings, face_encoding)
            print("face_distances", face_distances)

            best_match_index = np.argmin(face_distances)
            print("best_match_index", best_match_index)
            if matches[best_match_index]:
                name = faces_names[best_match_index]
            face_names.append(name)


			# ↓↓↓↓↓↓↓↓ falta essa parte ↓↓↓↓↓↓↓↓
    #process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top = int(top*4)
        right = int(right*4)
        bottom = int(bottom * 4)
        left = int(left * 4)
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Input text label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 0.5, (255, 255, 255), 1)
        # Display the resulting image
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    k = cv2.waitKey(60)
    if k == 27:
        break

# cv2.destroyAllWindows()
# video_capture.release()
