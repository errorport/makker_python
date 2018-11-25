import cv2

video_capture = cv2.VideoCapture("/dev/video2")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
	ret, frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags=cv2.CASCADE_SCALE_IMAGE
	)
	eyes = eyeCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags=cv2.CASCADE_SCALE_IMAGE
	)

	for (x, y, w, h) in faces:
		#cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
		actual_face = frame[y:y+h,x:x+w]
		actual_face = actual_face[:,::-1]
		actual_face[:,:,0:2]=0
		frame[y:y+h,x:x+w] = actual_face

	for (x, y, w, h) in eyes:
		#cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 80, 255), 2)
		actual_eye = frame[y:y+h,x:x+w]
		actual_eye = actual_eye[::-1,:]
		frame[y:y+h,x:x+w] = actual_eye

	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		#print(faces)
		break

video_capture.release()
cv2.destroyAllWindows()