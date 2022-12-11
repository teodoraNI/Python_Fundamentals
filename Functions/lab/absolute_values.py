numbers = input().split()
abs_nums = []
for num in numbers:
    num = abs(float(num))
    abs_nums.append(num)
print(abs_nums)