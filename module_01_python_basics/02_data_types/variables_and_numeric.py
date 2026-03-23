"""
Module 01 - Bài 2: Biến, int/float/complex, toán tử, math, ép kiểu.
"""

import math

# Biến và kiểu
count = 42
price = 19.99
large = 1_000_000
c1 = 3 + 4j
print(type(count), type(price), abs(c1))

# Số thực — độ chính xác
print(0.1 + 0.2)
print(round(0.1 + 0.2, 1) == 0.3)

# Toán tử
print(10 / 3, 10 // 3, 10 % 3, 2**10)

x = 10
x += 5
x *= 2
print("x sau += và *=:", x)

# math
print(math.ceil(4.2), math.floor(4.9), math.log(100, 10))

# Ép kiểu
s = "123"
n = int(s)
f = float("3.14")
print(n + 1, f)
