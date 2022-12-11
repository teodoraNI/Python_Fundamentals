n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    plants[plant] = [int(rarity), []]
while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break
    elif command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        if plant in plants:
            plants[plant][1].append(int(rating))
        else:
            print('error')
    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        if plant in plants:
            plants[plant][0] = int(new_rarity)
        else:
            print('error')
    elif command[0] == 'Reset':
        plant = command[1]
        if plant in plants:
            plants[plant][1] = []
        else:
            print('error')
print('Plants for the exhibition:')
for plant, value in plants.items():
    if len(plants[plant][1]) != 0:
        average_rating = sum(plants[plant][1])/len(plants[plant][1])
    else:
        average_rating = 0
    print(f'- {plant}; Rarity: {plants[plant][0]}; Rating: {average_rating:.2f}')


