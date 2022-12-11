import numpy as np


def find(element, matrix):
    for i, matrix_i in enumerate(matrix):
        for j, value in enumerate(matrix_i):
            if value == element:
                return i, j


rows = int(input())
items = []
for _ in range(rows):
    items += list(input())
matrix1 = np.array(items).reshape(rows, len(items)//rows)
counter_moves = 0
while True:
    i, j = find('k', matrix1)
    if i == 0 or i == rows - 1 or j == 0 or j == len(items) - 1:
        counter_moves += 1
        print(f'Kate got out in {counter_moves} moves')
        break
    elif matrix1[i, j-1] == ' ':
        counter_moves += 1
        matrix1[i, j-1] = 'k'
        matrix1[i, j] = '#'
    elif matrix1[i, j+1] == ' ':
        counter_moves += 1
        matrix1[i, j+1] = 'k'
        matrix1[i, j] = '#'
    elif matrix1[i-1, j] == ' ':
        counter_moves += 1
        matrix1[i-1, j] = 'k'
        matrix1[i, j] = '#'
    elif matrix1[i+1, j] == ' ':
        counter_moves += 1
        matrix1[i+1, j] = 'k'
        matrix1[i, j] = '#'
    else:
        print('Kate cannot get out')
        break
