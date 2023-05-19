import numpy as np
a=[1,2,3,4,5]
x = np.array(a)

# Find the type of x using the function type().
print(type(x))

# Find the shape of the array:
print(x.shape)

# Find the type of data in the array:
print(x.dtype)

# Find the mean of the array:
print(x.mean())

print(np.array([1,-1])*np.array([1,1]))
print(np.dot(np.array([1,-1]),np.array([1,1])))