from turtle import *
import time

penup()
pencolor("grey")
pensize(5)

for i in range(50, -50 + -1, -100):
    for j in range(-150, 150 + 1, 100):
        goto(j, i)
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

time.sleep(3)