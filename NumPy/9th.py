"""
Uses a special NumPy function that iterates through every single element without caring about dimensions.
# Using ??? (fill in the function name)
for element in ???(arr):
    print(element)
Question:
What NumPy function name should replace ??? to iterate through every element (one by one)?
What would be the output if arr = np.array([[1, 2, 3], [4, 5, 6]])?

"""

# ans:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
for element in np.nditer(arr):
    print(element)
