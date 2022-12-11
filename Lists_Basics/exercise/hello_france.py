items = input().split('|')
budget = float(input())
initial_budget = budget
prices = []
profit = 0.0
for item in items:
    details = item.split('->')
    if details[0] == 'Clothes' and float(details[1]) <= 50.0 and budget >= float(details[1])\
            or details[0] == 'Shoes' and float(details[1]) <= 35.0 and budget >= float(details[1])\
            or details[0] == 'Accessories' and float(details[1]) <= 20.50 and budget >= float(details[1]):
        budget -= float(details[1])
        prices.append(float(details[1]) * 1.4)
        profit += float(details[1]) * 0.4
        if budget <= 0:
            break
for i in range(len(prices)):
    print(f"{prices[i]:.2f}", end=' ')
print()
print(f"Profit: {profit:.2f}")
if initial_budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")