"""
Module 02 - Bài 1: So sánh tốc độ list Python vs ndarray (theo giáo trình).
"""

import time

import numpy as np

n = 500_000
python_list = list(range(n))
start = time.perf_counter()
_ = [x * 2 for x in python_list]
t_list = time.perf_counter() - start

numpy_array = np.arange(n, dtype=np.int64)
start = time.perf_counter()
_ = numpy_array * 2
t_np = time.perf_counter() - start

print(f"List comprehension ({n:,} phần tử): {t_list:.4f} s")
print(f"NumPy vectorized     ({n:,} phần tử): {t_np:.4f} s")
if t_np > 0:
    print(f"~ {t_list / t_np:.1f}x nhanh hơn (tùy máy)")
