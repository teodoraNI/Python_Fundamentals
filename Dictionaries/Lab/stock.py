stock = {}
products = input().split()
searched_items = input().split()
for index in range(0, len(products), 2):
    product = products[index]
    quantity = int(products[index + 1])
    stock[product] = quantity
for item in searched_items:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
