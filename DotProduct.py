import numpy as np
#matrix a
a = np.array([[1,2],[3,4]])

print("matrix a dimension ", a.shape)

#matrix b
b = np.array([[5,6,7],[8,9, 10]])

print("matrix b dimension ", b.shape)

#matrix c = a.b
c = np.dot(a,b)

print("dot product of a and b: ", c)

print("matrix c dimension ", c.shape)
