message = input()

while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        break
    elif command[0] == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in message:
            index = message.find(substring)
            to_be_added = substring[::-1]
            message = message[:index]+ message[index+len(substring):] + to_be_added
            print(message)
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)
        print(message)
print(f'You have a new text message: {message}')

