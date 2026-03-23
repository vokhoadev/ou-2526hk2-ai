"""
Module 02 - Bài 2 NumPy: thống kê (mean, std, sum), dot, transpose.
"""

import numpy as np

rng = np.random.default_rng(0)
x = rng.random((3, 4))
print("x:\n", x)
print("mean:", x.mean(), "std:", x.std(), "sum:", x.sum())
print("theo cột mean:", x.mean(axis=0))

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 0], [1, 3]])
print("a @ b:\n", a @ b)
print("dot:\n", np.dot(a, b))
print("transpose a.T:\n", a.T)
