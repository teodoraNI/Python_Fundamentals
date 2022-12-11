pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
max_health = int(input())
command = input()
stalemate = True
while command != 'Retire' and stalemate == True:
    action, *data = command.split()
    if action == 'Status':
        need_repair = [section for section in pirate_ship if section < max_health * 0.2]
        print(f'{len(need_repair)} sections need repair.')
    elif action == 'Fire':
        index, damage = list(map(int, data))
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                stalemate = False
    elif action == 'Defend':
        start_ind, end_ind, damage = list(map(int, data))
        if 0 <= start_ind < len(pirate_ship) and \
                start_ind <= end_ind and 0 <= end_ind < len(pirate_ship):
            for i in range(start_ind, end_ind+1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    stalemate = False
                    break
    elif action == 'Repair':
        index, health = list(map(int, data))
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health <= max_health:
                pirate_ship[index] += health
            else:
                pirate_ship[index] = max_health
    command = input()
if stalemate:
    print(f'Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(war_ship)}')
