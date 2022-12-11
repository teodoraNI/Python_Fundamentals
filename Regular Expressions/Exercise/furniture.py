import re

bought_furniture = []
total_cost = 0
while True:
    purchase = input()
    if purchase == "Purchase":
        break
    pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
    match = re.search(pattern, purchase)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")

