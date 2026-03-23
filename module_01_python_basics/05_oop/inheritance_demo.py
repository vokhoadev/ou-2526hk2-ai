"""
Module 01 - Bài 5: Kế thừa, ghi đè phương thức, super().
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name}: {self.speak()}"


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


class Puppy(Dog):
    def __init__(self, name, age_months):
        super().__init__(name)
        self.age_months = age_months

    def describe(self):
        base = super().describe()
        return f"{base} ({self.age_months} tháng tuổi)"


if __name__ == "__main__":
    d = Dog("Mực")
    c = Cat("Muối")
    p = Puppy("Con", 4)
    print(d.describe())
    print(c.describe())
    print(p.describe())
