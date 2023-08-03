from tkinter import *

def calCharge():
    cost = 0
    currentUnit = unit.get()

    cost += min(currentUnit, 10) * 5
    currentUnit -= 10
    if currentUnit > 0:
        cost += min(currentUnit, 20) * 4.5
        currentUnit -= 20
        if currentUnit > 0:
            cost += currentUnit * 4

    costLabel["text"] = "ยอดค่าไฟฟ้าสุทธิ: {cost} บาท".format(cost = cost)

app = Tk()
app.title("Electricity Bill Calculator")
app.minsize(300, 300)
app.maxsize(300, 300)

header = Label(app, text = "Electricity Bill Calculator", font = "JasmineUPC 20 bold italic")
header.pack()

space1 = Label(app)
space1.pack()

unitLabel = Label(app, text = "ไฟฟ้าที่ใช้")
unitLabel.pack()
unit = DoubleVar()
unitInputField = Entry(app, textvariable = unit)
unitInputField.pack()

space2 = Label(app)
space2.pack()

calButton = Button(app, text = "Calculate", command = calCharge, height = 2)
calButton.pack()

space3 = Label(app)
space3.pack()

costLabel = Label(app, text = "ค่าไฟฟ้าสุทธิ: 0 บาท", font = "bold")
costLabel.pack()

app.mainloop()