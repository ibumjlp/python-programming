from turtle import *
import time

def drawCircle(color, x, y):
    penup()
    goto(x, y)
    pencolor(color)
    pendown()
    circle(45)

pensize(5)

drawCircle("blue", -100, 0)
drawCircle("black", 0, 0)
drawCircle("red", 100, 0)
drawCircle("yellow", -50, -50)
drawCircle("green", 50, -50)

time.sleep(3)