list_nums = (input()).split(', ')
list_nums = [int(list_nums[i]) for i in range(len(list_nums))]
for i in range(len(list_nums)):
    if list_nums[i] == 0:
        list_nums.append(list_nums[i])
        list_nums.remove(0)
print(list_nums)