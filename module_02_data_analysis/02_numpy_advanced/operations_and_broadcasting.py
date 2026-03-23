"""
Module 02 - Bài 2 NumPy: phép toán phần tử, broadcasting, ufunc.
"""

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print("a + b:", a + b)
print("a * b:", a * b)
print("a ** 2:", a**2)

# So sánh
print("a > 2:", a > 2)

# ufunc
arr = np.array([1, 4, 9, 16])
print("sqrt:", np.sqrt(arr))

# Broadcasting
print("a + 10:", a + 10)
m = np.array([[1], [2], [3]])
v = np.array([10, 20, 30, 40])
print("m + v:\n", m + v)
