import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

scaling = 8
_cmap="cool"
pics = 10

matrix = np.zeros([62,62])

print(matrix)
print(matrix.shape)

for i in range(pics//2):
	for y in range(matrix.shape[0]):
		for x in range(matrix.shape[1]):
			matrix[y,x] = ((y+x) % (i+2)) * (x+y)
	matrix_to_export=np.kron(matrix, np.ones((scaling, scaling)))
	imnum = '{:03d}'.format(i)
	image.imsave(fname="makker-sakk_"+imnum+".png", arr=matrix_to_export, cmap=_cmap)

for i in range(pics//2):
	for y in range(matrix.shape[0]):
		for x in range(matrix.shape[1]):
			matrix[y,x] = ((y+x) % ((pics//2)-i+2)) * (x+y)
	matrix_to_export=np.kron(matrix, np.ones((scaling, scaling)))
	imnum = '{:03d}'.format(i+pics//2-1)
	image.imsave(fname="makker-sakk_"+imnum+".png", arr=matrix_to_export, cmap=_cmap)

print(matrix)
plt.imshow(matrix, interpolation="none", cmap="Greys_r")
plt.xticks([]), plt.yticks([])
#matrix_to_export=np.kron(matrix, np.ones((scaling, scaling)))
#image.imsave(fname="makker-sakk.jpg", arr=matrix_to_export, cmap="Greys_r")


#plt.show()

#input()
