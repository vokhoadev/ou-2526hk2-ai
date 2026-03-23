"""
Module 02 - Bài 1 NumPy: tạo mảng, dtype, shape, zeros/ones/arange/linspace.
"""

import numpy as np

print("NumPy version:", np.__version__)

arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("1D:", arr1d, "dtype:", arr1d.dtype)
print("2D:\n", arr2d, "shape:", arr2d.shape, "ndim:", arr2d.ndim)

zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
full = np.full((2, 3), 7)
print("zeros:\n", zeros)
print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))

rng = np.random.default_rng(42)
print("random int:", rng.integers(0, 10, size=(2, 3)))
print("random float:\n", rng.random((2, 3)))
