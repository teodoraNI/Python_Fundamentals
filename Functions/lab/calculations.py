def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return int(num1 / num2)


operation = input()
num1 = int(input())
num2 = int(input())
result = calculator(num1, num2, operation)
print(result)