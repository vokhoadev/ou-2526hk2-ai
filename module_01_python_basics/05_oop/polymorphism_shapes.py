"""
Module 01 - Bài 5: Đa hình — cùng interface, hành vi khác (gợi ý Lab Shape hierarchy).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    def describe(self) -> str:
        return f"{self.__class__.__name__}, diện tích ≈ {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return pi * self.r**2


if __name__ == "__main__":
    shapes: list[Shape] = [Rectangle(3, 4), Circle(2)]
    for s in shapes:
        print(s.describe())
