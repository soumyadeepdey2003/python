"""
Write Python code to:

Create a 1D NumPy array called arr1 containing the numbers [1, 2, 3, 4, 5].

Create a 2D NumPy array called arr2 containing the numbers:
[
  [10, 20, 30],
  [40, 50, 60]
]
Print:

The shape of each array (.shape)

The number of elements in each array (.size)

The data type of the arrays (.dtype)

Example Output:
arr1 shape: (5,)
arr1 size: 5
arr1 dtype: int64

arr2 shape: (2, 3)
arr2 size: 6
arr2 dtype: int64


"""



import numpy as np

arr1=np.array([1, 2, 3, 4, 5])
print(arr1)

arr2=np.array([
  [10, 20, 30],
  [40, 50, 60]
])
print(arr2)

print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
# It profile a tuple Of the shape That means Proper dimension For 1D  array It provides a single Element tuple  And for my 2D array It provide Dimension of row and calumn
print(arr2.shape) 
print(arr2.size)
print(arr2.dtype)


