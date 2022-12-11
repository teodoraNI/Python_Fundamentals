targets = list(map(int, input().split()))
counter = 0
while True:
    command = input()
    if command == 'End':
        break
    else:
        index = int(command)
        if 0 <= index < len(targets):
            if targets[index] == -1:
                continue
            counter += 1
            a = targets[index]
            targets[index] = -1
            for i in range(len(targets)):
                if targets[i] > a and targets[i] != -1:
                    targets[i] -= a
                elif targets[i] <= a and targets[i] != -1:
                    targets[i] += a
print(f"Shot targets: {counter} -> ", end='')
print(*targets)

