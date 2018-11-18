import cv2 #importáljuk az opencv csomagot
import numpy as np

frame = cv2.imread("buddha.jpg", 0)

for y in range(frame.shape[0]):
	for x in range(frame.shape[1]):
		max = frame.shape[0]+frame.shape[1]
		frame[y,x] = 255*(x+y)//max

cv2.imshow("cica_dha", frame)

#print(frame.shape)
#print(frame.min(), frame.max())
#print(frame)

cv2.imwrite("acidified_buddha.png", frame)

while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
