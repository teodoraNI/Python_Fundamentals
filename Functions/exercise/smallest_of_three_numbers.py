def smallest_int(a:list):
    return min(a)


num1 = int(input())
num2 = int(input())
num3 = int(input())
my_list = [num1, num2, num3]
result = smallest_int(my_list)
print(result)