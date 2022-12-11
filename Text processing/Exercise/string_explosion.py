list = list(input())
counter = 0
magnitude = 0
for i in range(len(list)):
    if list[i] == '>':
        magnitude += int(list[i+1])
        list[i+1] = '*'
        counter += 1
    elif list[i] == '*':
        continue
    else:
        if counter < magnitude:
            list[i] = '*'
            counter += 1
        elif counter == magnitude:
            continue
while '*' in list:
    list.remove('*')
print(*list, sep = '')

