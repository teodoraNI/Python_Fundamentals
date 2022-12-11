command = input()
price_without_taxes = 0.0
taxes = 0.0
total_price = 0.0
while command != "special" and command != "regular":
    price = float(command)
    if price <= 0:
        print("Invalid price!")
        command = input()
        continue
    price_without_taxes += price
    command = input()
taxes = price_without_taxes * 0.2
total_price = price_without_taxes + taxes
if command == "special":
    total_price *= 0.9
if price_without_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {price_without_taxes:.2f}$ "
          f"\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
