n = int(input())
for i in range(1, n+1):
    number = int(input())
    if number % 2 == 0:
        continue
    else:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")