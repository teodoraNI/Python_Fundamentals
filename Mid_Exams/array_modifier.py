nums = input()
list_nums = [int(x) for x in nums.split()]
command = input()
while command != 'end':
    operation = command.split()
    if operation[0] == 'swap':
        list_nums[int(operation[1])], list_nums[int(operation[2])] = \
            list_nums[int(operation[2])], list_nums[int(operation[1])]
    elif operation[0] == 'multiply':
        list_nums[int(operation[1])] *= list_nums[int(operation[2])]
    elif operation[0] == 'decrease':
        for i in range(len(list_nums)):
            list_nums[i] -= 1
    command = input()
print(*list_nums, sep=', ')