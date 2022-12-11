def grade(x):
    if 2 <= x <= 2.99:
        print('Fail')
    elif 3 <= x <= 3.49:
        print('Poor')
    elif 3.50 <= x <= 4.49:
        print('Good')
    elif 4.50 <= x <= 5.49:
        print('Very Good')
    elif 5.50 <= x <= 6.00:
        print('Excellent')
x = float(input())
grade(x)