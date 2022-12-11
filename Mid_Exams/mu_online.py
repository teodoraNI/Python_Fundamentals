health = 100
bitcoins = 0
game_over = False
dungeons_rooms = input().split('|')
for i in range(len(dungeons_rooms)):
    command, amount = dungeons_rooms[i].split(' ')
    if command == 'potion':
        if health + int(amount) <= 100:
            health += int(amount)
            add_health = int(amount)
        else:
            add_health = 100 - health
            health = 100
        print(f'You healed for {add_health} hp.\nCurrent health: {health} hp.')
    elif command == 'chest':
        bitcoins += int(amount)
        print(f'You found {amount} bitcoins.')
    else:
        health -= int(amount)
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.\nBest room: {i+1}')
            game_over = True
            break
if not game_over:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")






