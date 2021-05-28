string = input("Enter a string")
if len(string) > 1:
    new_string = string[0:2] + string[-2:]
    print(new_string)
else:
    print("Empty String")
