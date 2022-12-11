first_lst = input().split(', ')
second_lst = input().split(', ')
in_lst = [first for first in first_lst if any (first in second for second in second_lst)] # comprehension of the below nested loops
# for i in range(len(first_lst)):
#     for j in range(len(second_lst)):
#         if first_lst[i] in second_lst[j]:
#             in_lst.append(first_lst[i])
#             break
print(in_lst)