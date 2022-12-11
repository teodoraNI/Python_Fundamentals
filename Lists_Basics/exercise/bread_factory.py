initial_energy = 100
current_energy = initial_energy
coins = 100
factory_is_open = True
events = input().split('|')
for event in events:
    event = event.split('-')
    if event[0] == 'rest':
        if current_energy + int(event[1]) > 100:
            print(f"You gained {100 - current_energy} energy.")
            current_energy = 100
        else:
            current_energy += int(event[1])
            print(f"You gained {event[1]} energy.")
        print(f"Current energy: {current_energy}.")
    elif event[0] == 'order':
        if current_energy >= 30:
            print(f"You earned {event[1]} coins.")
            coins += int(event[1])
            current_energy -= 30
        else:
            print("You had to rest!")
            current_energy += 50
    else:
        if coins >= int(event[1]):
            print(f"You bought {event[0]}.")
            coins -= int(event[1])
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            factory_is_open = False
            break
if factory_is_open:
    print(f'Day completed! \nCoins: {coins}\nEnergy: {current_energy}')