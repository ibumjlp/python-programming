list = [1, 2, 4, 2, 5, 2, 4, 8]

for i in list:
    count = list.count(i)
    print("{i} => {count}".format(i = i, count = count))