def orders_calculation(product, num):
    if product == 'coffee':
        price = 1.5 * num
    elif product == 'water':
        price = 1 * num
    elif product == 'coke':
        price = 1.4 * num
    elif product == 'snacks':
        price = 2 * num
    return(f"{price:.2f}")

product = input()
num = int(input())
print(orders_calculation(product, num))