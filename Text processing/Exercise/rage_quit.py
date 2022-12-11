string = input()
current_string = ''
list = []
my_set = set()
for i in range(len(string)):
    if not string[i].isdigit():
        current_string += string[i].upper()
        my_set.add(string[i].upper())
    else:
        if i+1 < len(string) and string[i+1].isdigit():
            list.append(current_string * int(string[i:i+2]))
        else:
            list.append(current_string * int(string[i]))
        current_string = ''
print(f"Unique symbols used: {len(my_set)}")
print(*list, sep='')