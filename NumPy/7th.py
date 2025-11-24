"""

arr=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Write code to:
Reshape arr to shape (2, 6)
Reshape arr to shape (3, 4, 1)
Flatten arr into a 1D array
Print the shape after each operation

"""
# ans:

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr.shape)

arr1=np.reshape(arr,(2,6))
print(arr1)
print(arr1.shape)

arr2=np.reshape(arr,(3,4,1))
print(arr2)
print(arr2.shape)

arr3=np.reshape(arr,(arr1.size,))
print(arr3)
print(arr3.shape)


arr4=arr.reshape(-1)
print(arr4)
print(arr4.shape)