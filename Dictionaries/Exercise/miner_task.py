resources = dict()
while True:
    command = input()
    if command == 'stop':
        break
    quantity = int(input())
    if command not in resources.keys():
        resources[command] = 0
    resources[command] += quantity
for command, quantity in resources.items():
    print(f"{command} -> {quantity}")