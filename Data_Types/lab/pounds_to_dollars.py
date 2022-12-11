from forex_python.converter import CurrencyRates
amount = int(input())
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = amount * current_rate
print(result)