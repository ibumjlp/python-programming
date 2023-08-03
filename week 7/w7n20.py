iteration = int(input("Iteration = "))

for i in range(1, iteration + 1):
    string = ""
    for j in range(1, i):
        string += "    "
    for j in range(1, ((iteration + 1) - i) + 1):
        string += str(j) + " | "
    print(string)