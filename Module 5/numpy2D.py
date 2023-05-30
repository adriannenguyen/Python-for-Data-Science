import numpy as np

A=np.array([[11,12],[21,22],[31,32]])

# Find the type of x using the function type().
print(type(A))

# Find the shape of the array:
print(A.shape)

# Find the type of data in the array:
print(A.dtype)

# Find the second row of the numpy array A:
print(A[1])

# Multiply array A and B.
A=np.array([[11,12],[21,22]])
B=np.array([[1, 0],[0,1]])

print(A*B)

# Perform matrix multiplication on array A and B (order will not matter in this case).
print(np.dot(A,B))