from turtle import *
import time
import random

def drawCircle(color, x, y):
    penup()
    goto(x, y)
    pencolor(color)
    pendown()
    circle(random.randint(1, 200))

list = []
colorArray = ["blue", "black", "red", "yellow", "green"]
iteration = 2
pensize(5)

for i in range(iteration):
    x = int(input("Input X{num}: ".format(num = i + 1)))
    y = int(input("Input Y{num}: ".format(num = i + 1)))
    list.append([x, y])

for j in range(iteration):
    drawCircle(colorArray[random.randint(0, len(colorArray) - 1)], list[j][0], list[j][1])

time.sleep(3)