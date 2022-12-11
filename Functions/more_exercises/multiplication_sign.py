def multiplication_sign(list):
    counter_neg_nums = 0
    for num in list:
        if num == 0:
            return 'zero'
        elif num < 0:
            counter_neg_nums += 1
    if counter_neg_nums % 2 != 0:
        return 'negative'
    else:
        return 'positive'


number1 = int(input())
number2 = int(input())
number3 = int(input())
list_nums = [number1, number2, number3]
print(multiplication_sign(list_nums))