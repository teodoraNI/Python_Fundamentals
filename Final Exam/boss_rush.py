import re

number_of_inputs = int(input())
pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+\s{1}[A-Za-z]+)#'
for _ in range(number_of_inputs):
    data = input()
    result = re.search(pattern, data)
    if result:
        name = result.group(1)
        title = result.group(2)
        print(f'{name}, The {title}\n>> Strength: {len(name)}\n>> Armor: {len(title)}')
    else:
        print('Access denied!')