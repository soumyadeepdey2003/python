"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Write code to:Get the values where arr > 5

"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(np.where(arr>5))

"""
output : (array([ 5,  6,  7,  8,  9, 10, 11]),)
It proved the index Value In which The value inside the index Is greater than 5

"""

values = arr[arr > 5]
print("Values:", values)

"""
Values: [ 6  7  8  9 10 11 12]
It helped to print Direct values Getter than 5

"""

