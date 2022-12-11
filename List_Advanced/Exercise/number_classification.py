numbers = list(map(int, input().split(', ')))
pos_numbers = [num for num in numbers if num >= 0]
neg_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print('Positive: ', end='')
print(*pos_numbers, sep=', ')
print('Negative: ', end='')
print(*neg_numbers, sep=', ')
print('Even: ', end='')
print(*even_numbers, sep=', ')
print('Odd: ', end='')
print(*odd_numbers, sep=', ')
