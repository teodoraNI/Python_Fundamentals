def perfect_num_finder(num:int):
    sum_dividers = 0
    for divider in range(1, num//2 + 1):
        if num % divider == 0:
            sum_dividers += divider
    if sum_dividers == num:
        return"We have a perfect number!"
    else:
        return"It's not so perfect."


number = int(input())
result = perfect_num_finder(number)
print(result)

