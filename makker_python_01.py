import cv2
import numpy as np
import matplotlib.pyplot as plt

frame = cv2.imread("buddha.jpg", 0)
frame2 = frame.copy()
#print(frame)

n = False

for y in range(frame.shape[0]):
	for x in range(frame.shape[1]):
		p = frame[y,x]
		if n :
			frame[y,x]-=frame[y,x]//2
		else :
			frame[y,x]+=frame[y,x-1]//2
		n = not n
		frame[y:,x] -= p//100
		frame[:,x] += p//200

frame = frame2+(frame//10)

framex = np.matrix([[255, 0, 255], [0, 255, 0], [255, 0, 255]])
print(framex)
cv2.imshow('frame', framex)
plt.imshow(framex, cmap = 'rainbow_r', interpolation = 'none')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
