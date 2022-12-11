def sum_odd_even_digits(a:str):
    sum_even = 0
    sum_odd = 0
    for item in a:
        if int(item) % 2 == 0:
            sum_even += int(item)
        else:
            sum_odd += int(item)
    return sum_odd, sum_even


my_string = input()
sum_odd, sum_even = sum_odd_even_digits(my_string)
print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")