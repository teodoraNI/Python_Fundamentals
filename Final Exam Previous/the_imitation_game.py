message = input()
while True:
    command = input().split('|')
    if command[0] == "Decode":
        break
    elif command[0] == "Move":
        number_of_letters = int(command[1])
        if 0 < number_of_letters < len(message):
            message = message[number_of_letters:] + message[:number_of_letters]
    elif command[0] == "Insert":
        index, value = int(command[1]), command[2]
        if 0 <= index <= len(message):
            message = message[:index] + value + message[index:]
    elif command[0] == "ChangeAll":
        substring, replacement  = command[1], command[2]
        if substring in message:
            message = message.replace(substring, replacement)
print(f"The decrypted message is: {message}")
