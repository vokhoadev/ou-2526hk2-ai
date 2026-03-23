"""
Module 01 - Bài 3: if/elif/else, for, while, break, continue, range, enumerate.
"""

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D hoặc thấp hơn"
print("Điểm:", score, "-> Xếp loại:", grade)

age = 20
status = "người lớn" if age >= 18 else "vị thành niên"
print("Ternary:", status)

# for
for i in range(3):
    print("range:", i)

fruits = ["táo", "cam", "chuối"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# while
n = 3
while n > 0:
    print("n =", n)
    n -= 1

# break / continue
for x in range(10):
    if x == 2:
        continue
    if x == 6:
        break
    print(x, end=" ")
print()
