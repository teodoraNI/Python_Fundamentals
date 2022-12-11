energy = int(input())
command = input()
wins_counter = 0
game_ends = False
while command != 'End of battle':
    distance = int(command)
    if energy - distance >= 0:
        wins_counter += 1
        energy -= distance
        if wins_counter % 3 == 0:
            energy += wins_counter
    else:
        print(f'Not enough energy! Game ends with {wins_counter} won battles and {energy} energy')
        game_ends = True
        break
    command = input()
if game_ends == False:
    print(f'Won battles: {wins_counter}. Energy left: {energy}')
