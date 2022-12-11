budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
easter_bread_cost = flour_price + eggs_price + milk_price
colored_eggs = 0
easter_breads = 0
while budget > easter_bread_cost:
    budget = budget - easter_bread_cost
    easter_breads += 1
    colored_eggs += 3
    if easter_breads % 3 == 0:
        colored_eggs -= easter_breads - 2
print(f"You made {easter_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
