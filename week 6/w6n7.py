from turtle import *
import time

pensize(5)
pencolor("orange")

penup()
goto(-50, 0)
pendown()
circle(75)

penup()
goto(50, 0)
pendown()
circle(75)

penup()
goto(0, -75)
pendown()
circle(75)

time.sleep(3)