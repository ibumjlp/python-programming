sum = 0
iteration = 0

while (True):
    name = input("Name: ")
    score = int(input("Score: "))
    if (name == "-1" and score == -1):
        break
    sum += score
    iteration += 1

print("Average: " + str(sum / iteration))