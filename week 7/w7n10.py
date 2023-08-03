print("1=ฝาก")
print("2=ถอด")
print("3=แสดงเงิน")

menu = int(input("Menu: "))
value = float(input("Value: "))

myAccount = 5000.50

if menu == 1:
    print(myAccount + value)
elif menu == 2:
    print(myAccount - value)
else:
    print(myAccount)