import numpy as np

array1d = np.array([1,2,3,4])
print("Shape of array1d before reshaping: ", array1d.shape)
array1d = array1d.reshape(1,4)
print("Shape of array1d after reshaping: ", array1d.shape)
#rank of matrix can be found using np.linalg.matrix_rank() function
print("array1d is a matrix of rank {}".format(np.linalg.matrix_rank(array1d)))
