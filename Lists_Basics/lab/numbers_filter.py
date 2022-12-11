n = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'
numbers = [int(input()) for x in range(n)]

command = input()
filtered_nums = []
for number in numbers:
    filters_passes = (
        command == COMMAND_EVEN and number % 2== 0 or
        command == COMMAND_ODD and number % 2 != 0 or
        command == COMMAND_POSITIVE and number >=0 or
        command == COMMAND_NEGATIVE and number < 0
    )
    if filters_passes:
        filtered_nums.append(number)
print(filtered_nums)
