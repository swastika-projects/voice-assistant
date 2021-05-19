import cv2
import face_recognition
import numpy as np

def face_rec():
    video_capture = cv2.VideoCapture(0)

    dhruv_image = face_recognition.load_image_file('dhruv-test.jpeg')
    dhruv_face_encoding = face_recognition.face_encodings(dhruv_image)[0]

    atul_image = face_recognition.load_image_file('atul-test.jpeg')
    atul_face_encoding = face_recognition.face_encodings(atul_image)[0]

    swastika_image = face_recognition.load_image_file('swastika-test.jpeg')
    swastika_face_encoding = face_recognition.face_encodings(swastika_image)[0]

    # check if no face is being detected
    ''' if len(user_face_encoding) == 0:
        print('No face detected in training image') '''

    known_face_encodings = [dhruv_face_encoding, atul_face_encoding, swastika_face_encoding]
    known_face_names = ["Dhruv", "Atul", "Swastika"]

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]  # converts frame[BGR] to rgb_frame[RGB]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # if True in matches:
            ''' first_match_index = matches.index(True)
                name = known_face_names[first_match_index] '''
            cv2.rectangle(frame, (left, top), (right, bottom), (225, 0, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (225, 0, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (225, 225, 225), 1)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


