"""
Write code to:

Find the product of all elements (multiply all together)

Find the cumulative sum (running total)

Find the difference between consecutive elements

Print all results

"""
# ans:

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
sum=0
mul=1
for i in arr:
    sum=sum+i
    mul=mul*i

print(mul)
print(sum)
res =[]
for i in range(0,len(arr)-1):
    res.append(int(arr[i+1]-arr[i]))

print(res)


# Alternative option/
"""
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# 1. Product of all elements
product = np.prod(arr)
print("Product:", product)  # Output: 12000000

# 2. Cumulative sum (running total)
cum_sum = np.cumsum(arr)
print("Cumulative sum:", cum_sum)  # Output: [ 10  30  60 100 150]

# 3. Difference between consecutive elements
diff = np.diff(arr)
print("Differences:", diff)  # Output: [10 10 10 10]

"""