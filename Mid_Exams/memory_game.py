elements = input().split(' ')
command1 = input()
counter_rounds = 0
while command1 != 'end':
    counter_rounds += 1
    command = command1.split()
    index1, index2 = int(command[0]), int(command[1])
    if index1 < 0 or index2 < 0 or index1 >= len(elements) or index2 >= len(elements) or index1 == index2:
        elements.insert(len(elements) // 2, f"-{counter_rounds}a")
        elements.insert(len(elements) // 2 + 1, f"-{counter_rounds}a")
        print('Invalid input! Adding additional elements to the board')
        command1 = input()
        continue
    if elements[index1] == elements[index2]:
        element = elements.pop(min(index1, index2))
        elements.pop(max(index1, index2) - 1)
        print(f'Congrats! You have found matching elements - {element}!')
        if elements == []:
            print(f'You have won in {counter_rounds} turns!')
            break
    else:
        print('Try again!')
    command1 = input()
if elements != []:
    print('Sorry you lose :(')
    print(*elements)
