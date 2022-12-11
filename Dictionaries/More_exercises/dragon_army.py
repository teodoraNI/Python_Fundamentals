dragons = {}
dragons_num = int(input())
for _ in range(dragons_num):
    command = input().split()
    type, name = command[0], command[1]
    damage = int(command[2]) if command[2].isdigit() else 45
    health = int(command[3]) if command[3].isdigit() else 250
    armor = int(command[4]) if command[4].isdigit() else 10
    if type not in dragons.keys():
        dragons[type] = {name: [damage, health, armor]}
    else:
         dragons[type][name] = [damage, health, armor]
for type, name in dragons.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for name in dragons[type]:
        total_damage += dragons[type][name][0]
        total_health += dragons[type][name][1]
        total_armor += dragons[type][name][2]
    print(f"{type}::({total_damage/len(dragons[type]):.2f}"
          f"/{total_health/len(dragons[type]):.2f}/{total_armor/len(dragons[type]):.2f})")
    for name in dict(sorted(dragons[type].items(), key=lambda x: x[0])):
        print(f"-{name} -> damage: {dragons[type][name][0]}, health: {dragons[type][name][1]}, armor: {dragons[type][name][2]}")

