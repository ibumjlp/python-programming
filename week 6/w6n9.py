from turtle import *
import time

pensize(5)

penup()
goto(-100, 0)
pencolor("blue")
pendown()
circle(45)

penup()
goto(0, 0)
pencolor("black")
pendown()
circle(45)

penup()
goto(100, 0)
pencolor("red")
pendown()
circle(45)

penup()
goto(-50, -50)
pencolor("yellow")
pendown()
circle(45)

penup()
goto(50, -50)
pencolor("green")
pendown()
circle(45)

time.sleep(3)