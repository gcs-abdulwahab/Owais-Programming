def rectangles_area(x, y):
    return x * y

a = 25
b = 25
area = rectangles_area(a, b)
print(f"the area of this rectangle is = {area}")
if area <= 25 :
    print("and that is a short rectangle")
if area >= 25 and area <= 100:
    print("and that is a midium rectangle")
if area >= 100:
    print("and that is a large rectangle")