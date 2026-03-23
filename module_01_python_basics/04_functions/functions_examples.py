"""
Module 01 - Bài 4: Hàm, tham số mặc định, *args, **kwargs, lambda, scope.
"""

def greet():
    print("Xin chào Python!")


def add(a, b):
    return a + b


def introduce(name, age, city):
    print(f"Tôi là {name}, {age} tuổi, ở {city}")


def greet_name(name, greeting="Xin chào"):
    return f"{greeting}, {name}!"


def sum_all(*args):
    return sum(args)


def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"  {k}: {v}")


def complex_demo(a, b, *args, option=True, **kwargs):
    print("a, b:", a, b)
    print("args:", args)
    print("option:", option)
    print("kwargs:", kwargs)


# Lambda
double = lambda x: x * 2
print("double(5):", double(5))

pairs = [(1, "b"), (3, "a"), (2, "c")]
pairs.sort(key=lambda p: p[1])
print("sorted by second:", pairs)

if __name__ == "__main__":
    greet()
    print(add(5, 3))
    introduce(age=20, city="Hà Nội", name="An")
    print(greet_name("Bình"))
    print(greet_name("Cường", "Chào"))
    print("sum_all:", sum_all(1, 2, 3, 4))
    print_info(name="An", khoa="CNTT")
    complex_demo(1, 2, 3, 4, extra="ok", flag=False)
