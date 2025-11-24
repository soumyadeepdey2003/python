"""
Write code to:

Concatenate arr[10, 20, 30, 40, 50] with [60, 70]
Add two arrays element-wise: [1, 2, 3]+[10, 20, 30]
Multiply all elements by 2

"""

# ans:
import numpy as np
arr=np.array([10, 20, 30, 40, 50])
arr1=np.array([60,70])
result = np.concatenate((arr,arr1))
print(result)

arr2=np.array([1, 2, 3])
arr3=np.array([10, 20, 30])
a = np.add(arr2, arr3)
print(a)
b=np.multiply(arr,2)
print(b)
