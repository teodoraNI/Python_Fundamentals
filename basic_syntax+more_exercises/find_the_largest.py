numbers = list(input())
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort(reverse=True)
print(''.join(map(str, numbers)))




