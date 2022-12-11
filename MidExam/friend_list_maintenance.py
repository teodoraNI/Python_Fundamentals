usernames = input().split(', ')
command = input().split(' ')
blacklisted_names = 0
lost_names = 0
while command[0] != 'Report':
    if command[0] == 'Blacklist':
        name = command[1]
        if name in usernames:
            usernames[usernames.index(name)] = 'Blacklisted'
            blacklisted_names += 1
            print(f'{name} was blacklisted.')
        else:
            print(f'{name} was not found.')
    elif command[0] == 'Error':
        index = int(command[1])
        if 0 <= index < len(usernames) and usernames[index] != 'Blacklisted' and usernames[index] != 'Lost':
            lost = usernames[index]
            usernames[index] = 'Lost'
            lost_names += 1
            print(f'{lost} was lost due to an error.')
    elif command[0] == 'Change':
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(usernames):
            old_name = usernames[index]
            usernames[index] = new_name
            print(f'{old_name} changed his username to {new_name}.')
    command = input().split(' ')
print(f'Blacklisted names: {blacklisted_names}\nLost names: {lost_names}')
print(*usernames)

