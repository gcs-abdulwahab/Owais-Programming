list = [1972, 2000, 2025, 1964, 2004, 1992, 1994, 1996]
def is_leap_year(x):
    if x % 4 == 0:
        return True
    else:
        return False


for x in list:
    if is_leap_year(x)== True:
        print(f" {x}  is a Leap Year")
    else:
        print(f" {x}  is not a Leap Year")
