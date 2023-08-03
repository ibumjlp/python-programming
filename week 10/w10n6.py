dict = { 200:'a', 35:'b', 57:'c', 233:'e', 98:'d' }

sum = 0
for i in dict:
    sum += i

print("Average: " + str(sum / len(dict)))
print("Max: " + str(max(dict)))
print("Min: " + str(min(dict)))
print("Max's name: " + dict[max(dict)])
print("Min's name: " + dict[min(dict)])