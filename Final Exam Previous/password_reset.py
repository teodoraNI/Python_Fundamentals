def take_odd(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 != 0:
            new_string += string[i]
    return  new_string

def cut(string, index, length):
    new_string = string[:index] + string[index+length:]
    return new_string

def substitute(string, substring, substitution):
    new_string = string
    if substring in string:
        new_string = string.replace(substring, substitution)
        print(new_string)
    else:
        print('Nothing to replace!')
    return new_string


password = input()
while True:
    command = input()
    if command == 'Done':
        break
    elif command == 'TakeOdd':
        password = take_odd(password)
        print(password)
    else:
        data = command.split()
        if data[0] == 'Cut':
            index, length = int(data[1]), int(data[2])
            password = cut(password, index, length)
            print(password)
        elif data[0] == 'Substitute':
            substring, substitution = data[1], data[2]
            password = substitute(password, substring, substitution)
print(f'Your password is: {password}')