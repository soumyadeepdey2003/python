"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()

arr[0] = 100

print(x)
print(y)
print(x.base)
print(y.base)
What is the output?

"""
# ans:
"""
[1,2,3,4,5]
[100,2,3,4,5]
None
[100,2,3,4,5]

In this case when I use View Then it will refer to the original array With a new pointer y with arr That's why when 
we change the first element of arr It will also reflect two y But x Having a different Address and copy Data from arr That's Why Change in 
arr does not reflect In X And base of X is also giving None As it has Its new address But base of y Giving The original data present in the address of arr


"""