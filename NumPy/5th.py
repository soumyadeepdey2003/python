"""

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2
print(result)
What error will this code produce? Why?

"""

#ans:
"""
Element-wise addition (+) in NumPy only works for arrays that have compatible (ideally identical) shapes.
"""
