numbers = [int(x) for x in input().split(' ')]
average = sum(numbers)/len(numbers)
numbers.sort(reverse=True)
new_list = []
if len(numbers)>=5:
    length = 5
else: length = len(numbers)
for i in range(length):
    if numbers[i] > average:
        new_list.append(numbers[i])
if len(new_list) == 0:
    print("No")
else: print(*new_list)