def factors(n):
    print(f"factors of {n} :")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" , ")


def multiple(n):
    print(f"multiples of {n}:")
    for i in range(1, 11):
        print(f" {i * n}", end=' , ')


factors(600)
multiple(6)
