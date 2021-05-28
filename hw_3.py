lists = []
size = int(input("Enter size of the list:"))

for i in range(size):
    num = float(input("Enter number [" + str(i+1) + "]: "))
    lists.append(num)

print("The Largest Number From The List Is: ", max(lists))
