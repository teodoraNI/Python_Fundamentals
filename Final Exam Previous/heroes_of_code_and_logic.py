def register_hero(heroes, name, hitpoints, manapoints):
    heroes[name] = [hitpoints, manapoints]
    return heroes

def castspell(name, MPneeded, spellname):
    if heroes[name][1] >= int(MPneeded):
        heroes[name][1] -= int(MPneeded)
        print(f'{name} has successfully cast {spellname} and now has {heroes[name][1]} MP!')
    else:
        print(f'{name} does not have enough MP to cast {spellname}!')

def take_damage(name, damage, attacker):
    heroes[name][0] -= int(damage)
    if heroes[name][0] > 0:
        print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!')
    else:
        del heroes[name]
        print(f'{name} has been killed by {attacker}!')

def recharge(name, amount):
    heroes[name][1] += amount
    if heroes[name][1] > 200:
        amount -= heroes[name][1] - 200
        heroes[name][1] = 200
    print(f'{name} recharged for {amount} MP!')

def heal(name, amount):
    heroes[name][0] += amount
    if heroes[name][0] > 100:
        amount -= heroes[name][0] - 100
        heroes[name][0] = 100
    print(f'{name} healed for {amount} HP!')

number_of_heroes = int(input())
heroes = {}
for _ in range(number_of_heroes):
    name, HP, MP = input().split()
    register_hero(heroes,name, int(HP), int(MP))
while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        name, MPneed, spellname = command[1], command[2], command[3]
        castspell(name, MPneed, spellname)
    elif command[0] == 'TakeDamage':
        name, damage, attacker = command[1], command[2], command[3]
        take_damage(name, damage, attacker)
    elif command[0] == 'Recharge':
        name, amount = command[1], int(command[2])
        recharge(name, amount)
    elif command[0] == 'Heal':
        name, amount = command[1], int(command[2])
        heal(name, amount)
for key, value in heroes.items():
    print(f'{key}\n  HP: {heroes[key][0]}\n  MP: {heroes[key][1]}')




