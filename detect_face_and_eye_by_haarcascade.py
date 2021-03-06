##############################--------------DETECT FACE AND EYE BY HAARCASCADE---------------###########################


# Importing the libraries
import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (face_x, face_y, face_w, face_h) in faces:
        cv2.rectangle(frame, (face_x, face_y), (face_x+face_w, face_y+face_h), (255, 0, 0), 2)
        roi_gray = gray[face_y:face_y+face_h, face_x:face_x+face_w]
        roi_color = frame[face_y:face_y+face_h, face_x:face_x+face_w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (eye_x, eye_y, eye_w, eye_h) in eyes:
            cv2.rectangle(roi_color, (eye_x, eye_y), (eye_x+eye_w, eye_y+eye_h), (0, 255, 0), 2)
    return frame

# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
