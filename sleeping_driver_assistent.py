import cv2
import mediapipe as mp
import math
import time
import winsound

#EYES_LIST = [160, 144, 159, 145, 158, 153, 157, 154, 384, 381, 385, 380, 386, 374, 387, 373]
EYES_LIST = [159, 145]
HEAD_LIST = [6, 1]

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
width, height = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
n_pisc = 0
PISCA_FLAG = False
PISCA_THRES = 0.17
with mp_face_mesh.FaceMesh() as face_mesh:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print('Ignoring empty camera frame')
            continue

        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False
        results = face_mesh.process(frame)

        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:

            landmarks = results.multi_face_landmarks
            for face_landmarks in landmarks:
                d_eye = math.sqrt(
                    (face_landmarks.landmark[EYES_LIST[0]].x - face_landmarks.landmark[EYES_LIST[1]].x)**2 +
                    (face_landmarks.landmark[EYES_LIST[0]].y - face_landmarks.landmark[EYES_LIST[1]].y)**2
                )
                d_head = math.sqrt(
                    (face_landmarks.landmark[HEAD_LIST[0]].x - face_landmarks.landmark[HEAD_LIST[1]].x) ** 2 +
                    (face_landmarks.landmark[HEAD_LIST[0]].y - face_landmarks.landmark[HEAD_LIST[1]].y) ** 2
                )
                proportional_d = d_eye/d_head
                #print(proportional_d)
                if proportional_d < PISCA_THRES and not PISCA_FLAG:
                    n_pisc += 1
                    #print('piscou', n_pisc, 'vezes')
                    t = time.time()
                    PISCA_FLAG = True

                if PISCA_FLAG:
                    dif_t = time.time() - t
                    print('Olhos fechados... tempo = ' + str(int(dif_t)) + 's')
                    #print(dif_t)
                    if dif_t >= 1.0:
                        print('Pânico - DORMIU! -----------------------------------')
                        winsound.Beep(1000, 1000)
                if proportional_d > PISCA_THRES and PISCA_FLAG:
                    PISCA_FLAG = False
                    dif_t = time.time() - t

                cv2.circle(frame, (int(face_landmarks.landmark[EYES_LIST[0]].x * width),
                                   int(face_landmarks.landmark[EYES_LIST[0]].y * height)), 2, (0, 255, 255),
                           thickness=-1)
                cv2.circle(frame, (int(face_landmarks.landmark[EYES_LIST[1]].x * width),
                                   int(face_landmarks.landmark[EYES_LIST[1]].y * height)), 2, (0, 255, 255),
                           thickness=-1)

                cv2.circle(frame, (int(face_landmarks.landmark[HEAD_LIST[0]].x * width),
                                   int(face_landmarks.landmark[HEAD_LIST[0]].y * height)), 2, (0, 0, 255),
                           thickness=-1)
                cv2.circle(frame, (int(face_landmarks.landmark[HEAD_LIST[1]].x * width),
                                   int(face_landmarks.landmark[HEAD_LIST[1]].y * height)), 2, (0, 0, 255),
                           thickness=-1)
        cv2.imshow('MediaPipe Face Detection', frame)
        if cv2.waitKey(5) % 0xFF == 27:
            break
cap.release()
