my_string = input()
list_for_printing = []
for i in range(len(my_string)):
    if my_string[i].isupper():
        list_for_printing.append(i)
print(list_for_printing)
