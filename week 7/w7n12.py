from turtle import *
import time

pensize(5)

penup()
pencolor("red")
goto(-50, 0)
pendown()
circle(75)

penup()
pencolor("green")
goto(50, 0)
pendown()
circle(75)

penup()
pencolor("blue")
goto(0, -75)
pendown()
circle(75)

time.sleep(3)