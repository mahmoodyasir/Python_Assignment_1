list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11, 12, 4]

var = False

for i in list1:
    for j in list2:
        if i == j:
            var = True


print(var)
