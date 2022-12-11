import numpy as np

rows = int(input())
items = []
for _ in range(rows):
    items += list(map(int, input().split(' ')))
matrix = np.array(items).reshape(rows, len(items)//rows)
counter_destroyed_ships = 0
attacks = input().split(' ')
for attack in attacks:
    row, col = list(map(int, attack.split('-')))
    if matrix[row, col] > 0:
        matrix[row, col] -= 1
        if matrix[row, col] == 0:
            counter_destroyed_ships += 1
print(counter_destroyed_ships)




