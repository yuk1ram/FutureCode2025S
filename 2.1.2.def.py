import math

def get_area(a,b,c):
    p = (a+b+c) / 2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def is_correct_triangle(a,b,c):
    max_side = max(a,b,c)
    if max_side == a:
        return a < b + c
    elif max_side == b:
        return b < a + c
    elif max_side == c:
        return c < a + b
    return None

print("введите значения сторон треугольника")
a = int(input())
b = int(input())
c = int(input())

if is_correct_triangle(a,b,c):
    print("площадь треугольника =", get_area(a,b,c))
else:
    print("треугольник с данными сторонами не существует")