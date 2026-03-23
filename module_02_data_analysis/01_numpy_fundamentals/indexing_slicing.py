"""
Module 02 - Bài 1 NumPy: indexing, slicing, boolean indexing, reshape.
"""

import numpy as np

arr = np.arange(12).reshape(3, 4)
print("arr:\n", arr)
print("arr[0, 1]:", arr[0, 1])
print("cột 2:", arr[:, 2])
print("hàng 1-2, cột 1-3:\n", arr[1:3, 1:4])

mask = arr > 5
print("boolean mask:\n", mask)
print("arr[arr > 5]:", arr[mask])

flat = arr.flatten()
print("flatten:", flat)
print("reshape(2,6):\n", arr.reshape(2, 6))
