"""

Write code to:

For arr1:

Print the sum, mean, and median.

For arr2:

Print the maximum and minimum value.

Create a new array called arr1_squared, where each element of arr1 is squared (element-wise).

Create a new array called arr2_plus5 which adds 5 to each element of arr2.

"""

# ans:

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
total = np.sum(arr1)
average = np.mean(arr1)
middle = np.median(arr1)
rr1_squared = arr1 ** 2
print(middle)  
print(average)
print(total)
print(arr1)
print(rr1_squared)

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(np.max(arr2))
print(np.min(arr2))
arr2_plus5 = arr2 + 5
print(arr2)
print(arr2_plus5)