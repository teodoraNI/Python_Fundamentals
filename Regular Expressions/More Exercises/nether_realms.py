import re

demons = {x.strip():{'health':0, 'damage':0} for x in input().split(',')}
for demon in demons.keys():
    demons[demon]['health'] = sum(ord(item) for item in re.findall(r'[^\d+\-\*\/\.]', demon))
    damage = re.findall(r'[+-]?\d+[.\d]*', demon)
    if damage:
        demons[demon]['damage'] = sum(float(item) for item in re.findall(r'[+-]?\d+[.\d]*', demon))
        operators = re.findall(r'[*/]', demon)
        if operators:
            for operator in operators:
                if operator == '*':
                    demons[demon]['damage'] *= 2
                elif operator == '/':
                    demons[demon]['damage'] /= 2
for key, item in sorted(demons.items(), key=lambda x: x[0]):
    print(f"{key} - {demons[key]['health']} health, {demons[key]['damage']:.2f} damage")