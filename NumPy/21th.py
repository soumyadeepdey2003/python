"""
arr1 =[1, 2, 3, 4, 5]
arr2 =[4, 5, 6, 7, 8]
Perform the following set operations using NumPy and print the results:
Union: Print an array of all unique elements present in either arr1 or arr2.
Intersection: Print an array of elements present in both arr1 and arr2.
Difference: Print an array of elements present in arr1 but not in arr2.
Symmetric Difference: Print an array of elements that are present in either arr1 or arr2, but not in both.
Unique: Print an array of unique elements from the concatenation of arr1 and arr2.

"""

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])

# 1. Union: All unique elements from both arrays
union = np.union1d(arr1, arr2)
print("Union:", union)  # [1 2 3 4 5 6 7 8]

# 2. Intersection: Elements common to both
intersection = np.intersect1d(arr1, arr2)
print("Intersection:", intersection)  # [4 5]

# 3. Difference: Elements in arr1 not in arr2
difference = np.setdiff1d(arr1, arr2)
print("Difference (arr1 - arr2):", difference)  # [1 2 3]

# 4. Symmetric Difference: Elements in either arr1 or arr2 but not both
sym_diff = np.setxor1d(arr1, arr2)
print("Symmetric Difference:", sym_diff)  # [1 2 3 6 7 8]

# 5. Unique: Unique elements from concatenation
concat = np.concatenate((arr1, arr2))
unique = np.unique(concat)
print("Unique elements from concatenation:", unique)  # [1 2 3 4 5 6 7 8]
