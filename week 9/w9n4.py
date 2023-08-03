from turtle import *
import time

def drawDiamond(x, y):
    goto(x, y)
    pendown()
    right(45)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(45)
    penup()

penup()
pencolor("grey")
pensize(3)

for i in range(50, -50 + -1, -100):
    for j in range(-150, 150 + 1, 100):
        drawDiamond(j, i)

time.sleep(3)