string = input()
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = [int(item) for item in string if item in digits]
non_nums = [item for item in string if item not in digits]
take_nums = []
skip_nums = []
final_string = []
for i in range(len(nums)):
    if i % 2 == 0:
        take_nums.append(nums[i])
    else:
        skip_nums.append(nums[i])
for i in range(len(take_nums)):
    if 0 <= take_nums[i] <= len(non_nums):
        final_string = final_string + non_nums[0:take_nums[i]]
        if 0 <= skip_nums[i] + take_nums[i] < len(non_nums):
            non_nums = non_nums[take_nums[i]+skip_nums[i]::]
print(''.join(final_string))