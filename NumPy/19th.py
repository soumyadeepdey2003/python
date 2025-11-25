"""

arr1 =[12, 18, 36]
arr2=[15, 24, 60]
Find the LCM of arr1 and arr2 elementwise using NumPy
Find the GCD of arr1 and arr2 elementwise using NumPy
Print both results

"""

import numpy as np

arr1 = np.array([12, 18, 36])
arr2 = np.array([15, 24, 60])
lcm=np.lcm(arr1,arr2)
gcd=np.gcd(arr1,arr2)
print(lcm)
print(gcd)

