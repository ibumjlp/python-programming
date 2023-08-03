key = [1, 2, 1, 3, 4, 4, 2, 2, 3, 1]

a = [1, 3, 3, 4, 1, 2, 1, 2, 3, 1]
b = [3, 3, 1, 4, 1, 2, 1, 2, 1, 1]
c = [1, 3, 1, 3, 1, 2, 1, 2, 1, 1]

sum = 0
for i in range(len(key)):
    if (a[i] == key[i]):
        sum += 1
print("A " + str(sum))

sum = 0
for i in range(len(key)):
    if (b[i] == key[i]):
        sum += 1
print("B " + str(sum))

sum = 0
for i in range(len(key)):
    if (c[i] == key[i]):
        sum += 1
print("C " + str(sum))