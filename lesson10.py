from turtle import *
n =int (input("введите кол-во сторон"))
a = 180 - (180 * (n - 2) / n)

for i in range(n):
    forward(150)
    left(a)

exitonclick()