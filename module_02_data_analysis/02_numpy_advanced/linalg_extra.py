"""
Module 02 - Bài 2 NumPy: giải hệ tuyến tính, norm (mở rộng trong giáo trình).
"""

import numpy as np

# Ax = b
A = np.array([[3, 1], [1, 2]], dtype=float)
b = np.array([9, 8], dtype=float)
x = np.linalg.solve(A, b)
print("Nghiệm x:", x)
print("Kiểm tra A @ x:", A @ x)

print("norm L2 của vector:", np.linalg.norm(np.array([3, 4])))
