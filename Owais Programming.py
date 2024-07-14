def print_square(x, ch):
    for i in range(x):
        print(f" {ch}" * x)
c = 8
print_square(c, "+")
print("-" * (c*2))
