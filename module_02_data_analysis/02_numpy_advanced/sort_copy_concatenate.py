"""
Module 02 - Bài 2 NumPy: sort, copy vs view (lưu ý), vstack/hstack, concatenate.
"""

import numpy as np

arr = np.array([3, 1, 4, 1, 5])
print("sort:", np.sort(arr))
print("argsort:", np.argsort(arr))

a = np.arange(6).reshape(2, 3)
b = a[:, 1:2]
print("b là view của a?", np.may_share_memory(a, b))
c = a.copy()
c[0, 0] = 99
print("a[0,0] không đổi sau khi sửa bản copy:", a[0, 0])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print("vstack:\n", np.vstack((x, y)))
print("hstack:\n", np.hstack((x, y)))
print("concatenate axis=1:\n", np.concatenate((x, y), axis=1))
