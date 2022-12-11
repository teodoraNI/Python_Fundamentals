numbers = [int(x) for x in input().split()]
while True:
    command = input()
    if command == 'find':
        break
    decrypted_command = ''
    for i in range(len(command)):
        if i < len(numbers):
            j = i
        else:
            j = i %(len(numbers))
        decrypted_command += chr(ord(command[i]) - numbers[j])
    index_coordinates1 = decrypted_command.index('<') + 1
    index_coordinates2 = decrypted_command.index('>')
    coordinates = decrypted_command[index_coordinates1:index_coordinates2]
    decrypted_command_list = decrypted_command.split('&')
    type = decrypted_command_list[1]
    print(f'Found {type} at {coordinates}')



