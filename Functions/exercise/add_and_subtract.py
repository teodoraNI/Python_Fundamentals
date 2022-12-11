def sum_numbers(a,b):
    return a+b


def subtract(sum,c):
    return sum - c

def sum_and_subtract(a,b,c):
    sum = sum_numbers(a,b)
    return subtract(sum, c)


num1 = int(input())
num2 = int(input())
num3 = int(input())
sum_numbers(num1, num2)
result = sum_and_subtract(num1, num2, num3)
print(result)
