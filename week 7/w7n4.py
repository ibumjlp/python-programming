temperature = float(input("Input temperature: "))

if temperature >= 80:
    print("High")
elif (temperature >= 50 and temperature < 80):
    print("Medium")
else:
    print("Low")