lines = int(input())
total_liters = 0
for i in range(lines):
    liters = int(input())
    if total_liters + liters <= 255:
        total_liters += liters
    else:
        print("Insuffcient capacity!")
print(total_liters)