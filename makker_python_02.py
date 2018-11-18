import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

scaling = 4

matrix = np.zeros([34,34])

print(matrix)
print(matrix.shape)

for i in range(32):
	for y in range(matrix.shape[0]):
		for x in range(matrix.shape[1]):
			matrix[y,x] = ((y+x) % i) * (x+y)
	matrix_to_export=np.kron(matrix, np.ones((scaling, scaling)))
	image.imsave(fname="makker-sakk_"+str(i)+".png", arr=matrix_to_export, cmap="Greys_r")

print(matrix)
plt.imshow(matrix, interpolation="none", cmap="Greys_r")
plt.xticks([]), plt.yticks([])
#matrix_to_export=np.kron(matrix, np.ones((scaling, scaling)))
#image.imsave(fname="makker-sakk.jpg", arr=matrix_to_export, cmap="Greys_r")


#plt.show()

#input()
