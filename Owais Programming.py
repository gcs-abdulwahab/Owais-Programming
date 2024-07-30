def print_square(w,c):
    for i in range(w):
        print(f"{c} "  * w)

# print_square(4,'*')

numbers_list = [1,2,3,4,5,6,7,8,9,10,]
for item in numbers_list:
    print_square(item,'* ')
    print(".......................")