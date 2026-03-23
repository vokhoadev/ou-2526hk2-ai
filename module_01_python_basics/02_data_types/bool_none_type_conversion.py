"""
Module 01 - Bài 2: bool, None, toán tử logic, type(), isinstance, chuyển kiểu an toàn.
"""

print(True and False, True or False, not True)
print(bool(0), bool(""), bool([1]))

x = None
print(x is None, x == None)  # nên dùng `is None`

a = 5
print(type(a), isinstance(a, int))

# Chuyển kiểu (có thể lỗi nếu không hợp lệ — dùng try trong bài tập)
print(int("10"), float("3.14"), str(99))
