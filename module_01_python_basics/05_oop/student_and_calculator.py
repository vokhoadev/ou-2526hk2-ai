"""
Module 01 - Bài 5: Lớp, __init__, thuộc tính lớp/instance, method chaining.
"""


class Student:
    school = "Đại học Mở"

    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.gpa = 0.0

    def introduce(self):
        return f"Xin chào, tôi là {self.name}, MSSV: {self.student_id}"

    def study(self, subject):
        print(f"{self.name} đang học {subject}")

    def update_gpa(self, new_gpa):
        if 0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
        else:
            raise ValueError("GPA phải trong [0, 4.0]")


class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def add(self, num):
        self.value += num
        return self

    def subtract(self, num):
        self.value -= num
        return self


if __name__ == "__main__":
    s1 = Student("An", 20, "SV001")
    print(s1.introduce())
    s1.study("Python")
    s1.update_gpa(3.5)
    print("GPA:", s1.gpa, "| Trường:", Student.school)

    calc = Calculator(10)
    calc.add(5).subtract(3).add(2)
    print("Calculator value:", calc.value)
