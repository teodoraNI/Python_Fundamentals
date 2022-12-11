items = input().split(', ')
command = input().split(' - ')
while command[0] != 'Craft!':
    if command[0] == 'Collect':
        if command[1] not in items:
            items.append(command[1])
    elif command[0] == 'Drop':
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == 'Renew':
        if command[1] in items:
            items.append(command[1])
            items.remove(command[1])
    elif command[0] == 'Combine Items':
        old_item, new_item = command[1].split(':')
        for i in range(len(items)):
            if items[i] == old_item:
                items.insert(i+1,new_item)
    command = input().split(' - ')
print(', '.join(items))