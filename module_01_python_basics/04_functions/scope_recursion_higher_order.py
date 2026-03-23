"""
Module 01 - Bài 4: phạm vi biến (local/global), đệ quy, hàm bậc cao (map/filter).
"""

count = 0  # global


def demo_scope():
    local_x = 1
    global count
    count += 1
    print("trong hàm:", local_x, "count=", count)


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def apply_twice(f, x):
    return f(f(x))


def main():
    demo_scope()
    print("factorial(5):", factorial(5))
    nums = [1, 2, 3, 4]
    print("map x2:", list(map(lambda z: z * 2, nums)))
    print("filter chẵn:", list(filter(lambda z: z % 2 == 0, nums)))
    print("apply_twice (+3):", apply_twice(lambda v: v + 3, 10))


if __name__ == "__main__":
    main()
