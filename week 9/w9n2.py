from turtle import *
import time
import random

def drawSquare():
    size = random.randint(1, 200)
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    penup()

penup()
pencolor("grey")
pensize(5)

for i in range(6):
    drawSquare()

time.sleep(3)