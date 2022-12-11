def factorial(num:int):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    return factorial
def factorial_division(num1:int, num2:int):
    return f"{factorial(num1) / factorial(num2):.2f}"


number1 = int(input())
number2 = int(input())
result = factorial_division(number1, number2)
print(result)