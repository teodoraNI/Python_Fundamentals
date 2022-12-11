import numpy as np
# not solved!

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