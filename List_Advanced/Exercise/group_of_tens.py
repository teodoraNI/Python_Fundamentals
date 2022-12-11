nums = list(map(int, input().split(', ')))
max_num = max(nums)
groups = []
highest_group = max_num // 10 + 1
for i in range(1, highest_group + 1):
    groups.append([num for num in nums if i-1 < num / 10 <= i])
if groups[-1] == []:
    groups.pop()
for j in range(len(groups)):
    print(f"Group of {(j+1)*10}'s:", groups[j])