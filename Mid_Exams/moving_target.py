targets = list(map(int, input().split(' ')))
command = input()
while command != 'End':
    action, index, value = command.split(' ')
    index = int(index)
    value = int(value)
    if index < 0 or index >= len(targets):
        if action == 'Add':
            print('Invalid placement!')
        if action == 'Strike':
            print('Strike missed!')
        command = input()
        continue
    if action == 'Shoot':
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)
    elif action == 'Add':
        targets.insert(index, value)
    elif action == 'Strike':
        if index - value < 0 or index + value >= len(targets):
            print('Strike missed!')
        else:
            for i in range(2*value+1):
                targets.pop(index-value)
    command = input()
print(*targets, sep='|')

