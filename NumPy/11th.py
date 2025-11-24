
"""
Write code to:
Stack arr1 and arr2 horizontally (side by side)
Stack arr1 and arr2 vertically (one on top of the other)
Print the shape of each result

"""


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

h=np.hstack((arr1,arr2))
v=np.vstack((arr1,arr2))

print(h)
print(h.shape)

print(v)
print(v.shape)