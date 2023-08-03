score = float(input("Input score: "))

if score >= 80:
    print("A")
elif (score >= 70 and score < 80):
    print("B")
elif (score >= 60 and score < 70):
    print("C")
elif (score >= 50 and score < 60):
    print("D")
else:
    print("F")