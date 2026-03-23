"""
Module 01 - Bài 3: List comprehension (và dict comprehension cơ bản).
"""

squares = [x**2 for x in range(5)]
print("squares:", squares)

evens = [x for x in range(10) if x % 2 == 0]
print("evens:", evens)

labels = [f"item_{i}" for i in range(3)]
print(labels)

word = "python"
positions = {ch: i for i, ch in enumerate(word)}
print("dict comp:", positions)
