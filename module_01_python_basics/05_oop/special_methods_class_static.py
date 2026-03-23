"""
Module 01 - Bài 5: __str__ / __repr__, __add__, @classmethod, @staticmethod.
"""

from __future__ import annotations


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    @classmethod
    def from_tuple(cls, t: tuple[float, float]) -> Vector2D:
        return cls(t[0], t[1])

    @staticmethod
    def dot(a: Vector2D, b: Vector2D) -> float:
        return a.x * b.x + a.y * b.y


if __name__ == "__main__":
    u = Vector2D(1, 2)
    v = Vector2D.from_tuple((3, 4))
    print("repr:", repr(u))
    print("str:", str(u))
    print("u + v:", u + v)
    print("dot:", Vector2D.dot(u, v))
