quantity = int(input())
days_until_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
spendings = 0
spirit = 0
for day in range(1, days_until_christmas+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        spendings += ornament_set_price * quantity
        spirit += 5
    if day % 3 == 0:
        spendings += (tree_skirt_price + tree_garland_price) * quantity
        spirit += 13
    if day % 5 == 0:
        spendings += tree_lights_price * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        spendings += tree_skirt_price + tree_garland_price + tree_lights_price
if days_until_christmas % 10 == 0:
    spirit -= 30
print(f"Total cost: {spendings}")
print(f"Total spirit: {spirit}")

