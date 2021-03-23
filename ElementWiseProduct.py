import numpy as np
#matrix a
a = np.array([[1,2],[3,4]])

print("matrix a dimension ", a.shape)

#matrix b
b = np.array([[5,6],[8,9]])

print("matrix b dimension ", b.shape)

#matrix c = a * b
c = np.multiply(a,b)

print("element wise product of matrices a and b: ", c)

print("matrix c dimension ", c.shape)
