import numpy as np

# Check the type of the array and Value type for the given array c
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))
print(b.dtype)  

# Assign the value 20 for the second element in the given array.
a = np.array([10, 2, 30, 40,50])
a[1] = 20
print(a)

# Print the even elements in the given array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])

# Find the size ,dimension and shape for the given array b
b = np.array([10, 20, 30, 40, 50, 60, 70])
print(b.size)
print(b.ndim)
print(b.shape)

# Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])
print(c.max())
print(c.min())

# Perform addition operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = np.add(arr1, arr2)

# Perform subtraction operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = np.subtract(arr1, arr2)

# Perform multiply operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])

arr3 = np.multiply(arr1, arr2)

# Perform division operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

arr3 = np.divide(arr1, arr2)

# Perform dot operation on the given numpy array ar1 and ar2:
arr1 = np.array([3, 5])
arr2 = np.array([2, 4])

np.dot(arr1, arr2)

# Add Constant 5 to the given numpy array ar:
arr = np.array([1, 2, 3, -1]) 
arr + 5
