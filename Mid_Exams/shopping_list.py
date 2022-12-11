groceries = input().split('!')
command = input()
while command != 'Go Shopping!':
    order = command.split(' ')
    if order[0] == 'Urgent' and order[1] not in groceries:
        groceries.insert(0,order[1])
    elif order[0] == 'Unnecessary' and order[1] in groceries:
        groceries.remove(order[1])
    elif order[0] == 'Correct' and order[1] in groceries:
        for i in range(len(groceries)):
            if groceries[i] == order[1]:
                groceries[i] = order[2]
    elif order[0] == 'Rearrange' and order[1] in groceries:
        groceries.remove(order[1])
        groceries.append(order[1])
    command = input()
print(', '.join(groceries))






