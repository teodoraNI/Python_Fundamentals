import re

total_income = 0
while True:
    data = input()
    if data == "end of shift":
        break
    pattern = r'%([A-Z][a-z]+)%[^\|\$%\.]*<(\w+)>[^\|\$%\.]*\|(\d+)\|[^\d\|\$%\.)]*(\d+\.?\d*)\$'
    match = re.search(pattern, data)
    if match:
        name, product, quantity, price = match.groups()
        print(f'{name}: {product} - {int(quantity)*float(price):.2f}')
        total_income += int(quantity)*float(price)
print(f'Total income: {total_income:.2f}')