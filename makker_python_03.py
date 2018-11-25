import cv2
import sys

cascPath_face = sys.argv[1]
cascPath_eye = sys.argv[2]

faceCascade = cv2.CascadeClassifier(cascPath_face)
eyeCascade = cv2.CascadeClassifier(cascPath_eye)
#/home/bencsikg/.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt.xml
#/home/bencsikg/.local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml


video_capture = cv2.VideoCapture(2)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		flags = cv2.CASCADE_SCALE_IMAGE
    )
    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 100, 255), 5)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
