treasures = input().split('|')
info = input()
while info != 'Yohoho!':
    command, *data = [x for x in info.split()]
    if command == 'Loot':
        for item in data:
            if item not in treasures:
                treasures.insert(0,item)
    elif command == 'Drop':
        index = int(data[0])
        if index >= 0 and index < len(treasures):
            treasures.append(treasures.pop(index))
    elif command == 'Steal':
        count = int(data[0])
        if count >= len(treasures):
            stolen = treasures.copy()
            treasures.clear()
        else:
            stolen = treasures[-count:]
            treasures = treasures[:-count]
        print(*stolen, sep=', ')
    info = input()
if not treasures:
    print('Failed treasure hunt.')
else:
    average_gain = sum(len(x) for x in treasures) / len(treasures)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')