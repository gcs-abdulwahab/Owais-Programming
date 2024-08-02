def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


list = [2, 3, 4, 5, 6]

for item in list:
    if is_even(item):
        print(f"This item is even so I will print square {square(item)}")
    else:
        print(f"This item odd so I will print the cube {cube(item)}")
