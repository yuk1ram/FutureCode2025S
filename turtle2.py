from turtle import *

n = input()
if n == "круг":
    circle(200)
elif n == ("квадрат"):
    circle(200)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)

else:
    penup()
    setx(-100)
    sety(100)
    right(45)
    pendown()
    setx(100)
    sety(100)
    right(60)
    pendown()
    forward(400)

exitonclick()
