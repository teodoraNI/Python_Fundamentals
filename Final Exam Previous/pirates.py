def register_target(list, target, people, wealth):
    if target not in list.keys():
        list[target] = [int(people), int(wealth)]
    else:
        list[target][0] += int(people)
        list[target][1] += int(wealth)
    return list

def plunder(list, target, people, wealth):
    list[target][0] -= int(people)
    list[target][1] -= int(wealth)
    print(f"{target} plundered! {wealth} gold stolen, {people} citizens killed.")
    if list[target][0] <= 0 or list[target][1] <= 0:
        del list[target]
        print(f"{target} has been wiped off the map!")

def prosper(list, target, wealth):
    if wealth.startswith('-'):
        return print("Gold added cannot be a negative number!")
    else:
        list[target][1] += int(wealth)
        return print(f"{wealth} gold added to the city treasury. {target} now has {list[target][1]} gold.")


targets = {}
command = input()
while command != 'Sail':
    city, population, gold = command.split('||')
    register_target(targets, city, population, gold)
    command = input()
data = input().split('=>')
while data[0] != "End":
    if data[0] == "Plunder":
        plunder(targets, data[1], data[2], data[3])
    elif data[0] == "Prosper":
        prosper(targets, data[1], data[2])
    data = input().split('=>')
if targets == {}:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for city in targets:
        print(f"{city} -> Population: {targets[city][0]} citizens, Gold: {targets[city][1]} kg")





