def position_in_alphabet(letter):
    return ord(letter) - 96

data = input().split()
result = 0
for item in data:
    a = position_in_alphabet(item[0].lower())
    b= position_in_alphabet(item[-1].lower())
    if item[0].isupper():
        result += int(item[1:-1])/a
    else:
        result += int(item[1:-1]) * a
    if item[-1].isupper():
        result -= b
    else:
        result += b
print(f"{result:.2f}")

