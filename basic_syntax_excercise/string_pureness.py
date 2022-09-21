strings_number = int(input())
for string in range(strings_number):
    string = input()
    if '.' in string or ',' in string or '_' in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")