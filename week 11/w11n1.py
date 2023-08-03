from tkinter import *

data = []

def saveData():
    record = [id.get(), name.get(), score.get()]
    data.append(record)

    id.set("")
    name.set("")
    score.set(0)

def calData():
    scoreList = []
    sum = 0
    
    for i in range(len(data)):
        scoreList.append(data[i][2])
        sum += data[i][2]

    avgLabel["text"] = "ค่าเฉลี่ยคะแนน: {avg}".format(avg = sum / len(scoreList))
    maxLabel["text"] = "ค่าสูงสุด: {max}".format(max = max(scoreList))
    minLabel["text"] = "ค่าต่ำสุด: {min}".format(min = min(scoreList))
  
app = Tk()
app.title("Simple GUI: w11n1")
app.minsize(400, 400)
app.maxsize(400, 400)

# b1 = Button(app, text = 'Exit', command = app.destroy)
# b1.pack()

# x1 = StringVar()
# x2 = IntVar()
# x3 = DoubleVar()
# x4 = BooleanVar()

header = Label(app, text = "My App", font = "JasmineUPC 20 bold italic")
header.pack()

space1 = Label(app)
space1.pack()

idLabel = Label(app, text = "รหัสนักศึกษา")
idLabel.pack()
id = StringVar()
idInputField = Entry(app, textvariable = id)
idInputField.pack()

nameLabel = Label(app, text = "ชื่อ")
nameLabel.pack()
name = StringVar()
nameInputField = Entry(app, textvariable = name)
nameInputField.pack()

scoreLabel = Label(app, text = "คะแนน")
scoreLabel.pack()
score = DoubleVar()
scoreInputField = Entry(app, textvariable = score)
scoreInputField.pack()

space2 = Label(app)
space2.pack()

saveButton = Button(app, text = "Save", command = saveData)
saveButton.pack()

space3 = Label(app)
space3.pack()

calButton = Button(app, text = "Calculate", command = calData)
calButton.pack()

space4 = Label(app)
space4.pack()

avgLabel = Label(app, text = "ค่าเฉลี่ยคะแนน: 0")
avgLabel.pack()
maxLabel = Label(app, text = "ค่าสูงสุด: 0")
maxLabel.pack()
minLabel = Label(app, text = "ค่าต่ำสุด: 0")
minLabel.pack()

app.mainloop()