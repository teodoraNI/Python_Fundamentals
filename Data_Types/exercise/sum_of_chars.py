symbols = int(input())
total_sum = 0
for i in range(symbols):
    symbol = input()
    total_sum += ord(symbol)
print(f"The sum equals: {total_sum}")
