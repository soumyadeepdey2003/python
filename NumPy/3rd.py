"""

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr2[1])
print(arr2[:, 2])
print(arr1[arr1 % 2 == 0])
print(arr1[arr1 > 2])

What is the output?

"""
#ans:

"""
[40 50 60]

[30 60]

[2 4]

[3 4 5]

"""