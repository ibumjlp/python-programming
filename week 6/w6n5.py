from turtle import *
import time

center = float(input("Input center: "))
radius = float(input("Input radius: "))

pensize(5)
pencolor("blue")

penup()
setx(center)
sety(center)

pendown()
circle(radius)
penup()

time.sleep(3)