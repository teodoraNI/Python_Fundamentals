numbers = (input()).split()
list1 = [int(numbers[i]) for i in range(len(numbers))]
nums_to_remove = int(input())
if len(list1) <= nums_to_remove:
    exit
else:
    for i in range(nums_to_remove):
        min_num = min (list1)
        list1.remove(min_num)
print(*list1, sep=', ')

