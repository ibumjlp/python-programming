from turtle import *
import time

pensize(20)
pencolor("black")
goto(0, -350)

penup()
color("red", "red")
begin_fill()

goto(-50, 160)
pendown()
goto(50, 160)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)
forward(100)
right(45)

end_fill()
penup()
home()
pencolor("white")
write("STOP", True, align="center", font=("Arial", 45, "bold"))
pensize(8)

goto(-42, 142)
pendown()
goto(42, 142)
right(45)
forward(84)
right(45)
forward(84)
right(45)
forward(84)
right(45)
forward(84)
right(45)
forward(84)
right(45)
forward(84)
right(45)
forward(84)
right(45)

time.sleep(3)
