number = int(input())
sum = 0
for number in range (1, number+1):
    number_as_str = str(number)
    is_special = False
    for digit in range(len(number_as_str)):
        sum += int(number_as_str[digit])
    if sum in (5, 7, 11):
        is_special = True
    print(f"{number} -> {is_special}")
    sum = 0