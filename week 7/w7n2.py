from math import pi

radius = int(input("Input radius: "))

if radius < 0:
    print("number < 0")
else:
    answer = ((pi * radius) ** 2)
    print("%.2f" % answer)