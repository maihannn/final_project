# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

import cv2
import time
import datetime

capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_time_stopped= None
timer_starts = False
SECONDS_TO_RECORD_AFTER_DETECTION = 10

frame_size = (int(capture.get(3)), int(capture.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    _, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, width, height) in faces:
        cv2.rectangle (frame, (x,y), (x + width, y + height), (255, 0, 0), 2)
    for (x, y, width, height) in bodies:
        cv2.rectangle (frame, (x,y), (x + width, y + height), (0, 255, 0), 2)

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_starts = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Start Recording!")
    elif detection:
        if timer_starts:
            if time.time() - detection_time_stopped >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_starts = False
                out.release()
                print('Stop Recording!')
        else:
            timer_starts= True
            detection_time_stopped = time.time()

    if detection:
        out.write(frame)
    
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('h'):
        break

out.release()
capture.release()
cv2.destroyAllWindows()

