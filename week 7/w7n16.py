from turtle import *
import time
import random

penup()
pencolor("grey")
pensize(5)

for i in range(0, 4):
    size = random.randint(1, 200)
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()
    right(45)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(45)
    penup()

time.sleep(3)