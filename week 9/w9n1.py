def calculation(num1, num2, num3):
    power = num1 ** 2
    add = num2 + 100
    subtract = num3 - 50
    return power, add, subtract

input1 = int(input("Input 1: "))
input2 = int(input("Input 2: "))
input3 = int(input("Input 3: "))
answer = calculation(input1, input2, input3)

print(answer)