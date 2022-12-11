number = int(input())
if number in range(1,2,3):
    print("True")
for i in range(2, number):
    if number % i == 0:
        print("False")
        break
else:
    print("True")