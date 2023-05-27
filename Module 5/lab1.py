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

# Make a numpy array within [5, 4] and 6 elements
np.linspace(5, 4, num=6)

# Implement the following vector subtraction in numpy: u-v
u = np.array([1, 0])
v = np.array([0, 1])

u-v

# Multiply the numpy array z with -2:
z = np.array([2, 4])

z*-2

# Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. 
# Cast both lists to a numpy array then multiply them together:
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])

a*b

# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. 
# Then, plot the arrays as vectors using the fuction Plotvec2 and find their dot product:
import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
%matplotlib inline  

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))

# Convert the list [1, 0] and [0, 1] to numpy arrays a and b. 
# Then, plot the arrays as vectors using the function Plotvec2 and find their dot product:

a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))

# Convert the list [1, 1] and [0, 1] to numpy arrays a and b. 
# Then plot the arrays as vectors using the fuction Plotvec2 and find their dot product:

a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))

# Why are the results of the dot product for [-1, 1] and [1, 1] and the dot product for [1, 0] and [0, 1] zero, 
# but not zero for the dot product for [1, 1] and [0, 1]?
# The vectors used for question 4 and 5 are perpendicular. As a result, the dot product is zero.

# Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2. 
# Then perform Addition , Subtraction , Multiplication , Division and Dot Operation on the arr1 and arr2.
arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

arr3 = np.add(arr1, arr2)
arr4 = np.subtract(arr1, arr2)
arr5 = np.multiply(arr1, arr2)
arr6 = np.divide(arr1, arr2)
arr7 = np.dot(arr1, arr2)

# Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2. 
# Then find the even and odd numbers from arr1 and arr2.
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

even_arr1 = arr1[1:5:2]
odd_arr1= arr1[0:5:2]
even_arr2 = arr2[0:5:2]
odd_arr2 = arr2[1:5:2]