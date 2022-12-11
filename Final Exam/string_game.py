text = input()
while True:
    command = input().split()
    if command[0] == 'Done':
        break
    elif command[0] == 'Change':
        char, replacement = command[1], command[2]
        text = text.replace(char, replacement)
        print(text)
    elif command[0] == 'Includes':
        substring = command[1]
        if substring in text:
            print('True')
        else:
            print('False')
    elif command[0] == 'End':
        substring = command[1]
        print(text.endswith(substring))
    elif command[0] == 'Uppercase':
        text = text.upper()
        print(text)
    elif command[0] == 'FindIndex':
        char = command[1]
        print(text.find(char))
    elif command[0] == 'Cut':
        start_index, count = int(command[1]), int(command[2])
        text = text[start_index:start_index+count]
        print(text)


