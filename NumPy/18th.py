"""
arr_deg=[0, 30, 45, 60, 90]
Write code to:
Convert degrees in arr_deg to radians using NumPy
Compute the sine of each value (in radians)
Print both results

"""

import numpy as np

arr_deg = np.array([0, 30, 45, 60, 90])

# 1. Convert degrees to radians
arr_rad = np.deg2rad(arr_deg)
print("Radians:", arr_rad)
# 2. Compute sine of each radian value
sin_values = np.sin(arr_rad)
print("Sine values:", sin_values)