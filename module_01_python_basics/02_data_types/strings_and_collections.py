"""
Module 01 - Bài 2: Chuỗi, list/tuple/dict/set, toán tử so sánh & logic.
"""

# Chuỗi
s1 = "Python"
s2 = 'OU'
multi = """Nhiều
dòng"""
path = r"C:\Users\example"
print(s1 + " " + s2, len(s1), s1.upper(), "Py" in s1)
print(f"Chào {s1}: {2 + 3}")

# List
nums = [1, 2, 3]
nums.append(4)
print(nums[0], nums[-1], nums[1:3])

# Tuple (bất biến)
point = (10, 20)
print(point)

# Dict
student = {"name": "An", "age": 20}
print(student["name"], student.get("gpa", 0))

# Set
unique = {1, 2, 2, 3}
print(unique)

# Logic
age, income = 25, 50000
print(age >= 18 and income >= 30000)
