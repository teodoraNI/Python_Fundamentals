command = input()
products = {}
while command != "buy":
    name, price, quantity = command.split(' ')
    if name not in products:
        products[name] = [0, 0]
    products[name][0] = float(price)
    products[name][1] += int(quantity)
    command = input()
for name, value in products.items():
    print(f"{name} -> {products[name][0]*products[name][1]:.2f}")

