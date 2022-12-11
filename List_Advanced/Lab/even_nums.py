numbers = list(map(int, input().split(', ')))
indices_even_nums = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(indices_even_nums)