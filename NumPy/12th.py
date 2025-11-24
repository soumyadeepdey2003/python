"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

result = np.array_split(arr, 3)

print(result)
print(len(result))
print(result[0])
print(result[2])
What is the output?

"""

# ans:

"""

[array([1, 2]), array([3, 4]), array([5, 6])]
3
[1 2]
[5 6]

"""

