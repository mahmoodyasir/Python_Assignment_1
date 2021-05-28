lists = []
size = int(input("Enter size of the list:"))

for i in range(size):
    num = int(input("Enter number [" + str(i+1) + "]: "))
    lists.append(num)

lists = list(dict.fromkeys(lists))
print(lists)
