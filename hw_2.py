string = input("Enter a string")
length = len(string)
if length > 0:
    if 'not' in string and 'poor' in string:
        index1 = string.index('not')
        index2 = (string.index('poor') + 4)
        if index1 < index2:
            new_string = string.replace(string[index1:index2], 'good')
            print(new_string)
        else:
            print(string)

    else:
        print(string)

else:
    print("Provide a valid input")
    exit(0)



