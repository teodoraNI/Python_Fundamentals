command = input()
stock = {}
while command != 'statistics':
    product, quantity = command.split(": ")
    if product not in stock:
        stock[product] = 0
    stock[product] += int(quantity)
    command = input()
print("Products in stock:")
for (product, quantity) in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")

