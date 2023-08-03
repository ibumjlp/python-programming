from turtle import *
import time
from math import fabs

x1 = float(input("Input X1: "))
x2 = float(input("Input X2: "))

color("black", "light blue")
begin_fill()

penup()
goto(x1, 0)
pendown()

goto(x2, 0)
right(90)
forward(75)
right(90)
forward(fabs(x1 - x2))
right(90)
forward(75)

end_fill()

time.sleep(3)