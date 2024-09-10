def tables(x, y):
    for i in range(1, y + 1):
        print(f"{x} * {i} = {x * i}")


x = 16
for i in range(1, x + 1):
    tables(i, 10)
    print("- " * x)
