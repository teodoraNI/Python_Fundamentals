string = input()
digits = []
letters = []
symbols = []
for char in string:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        symbols.append(char)
print(*digits, sep= '')
print(*letters, sep= '')
print(*symbols, sep= '')

