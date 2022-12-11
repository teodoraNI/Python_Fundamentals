houses = list(map(int, input().split('@')))
command = input().split()
cupid_position = 0
count = 0
while command[0] != 'Love!':
    jump = int(command[1])
    if cupid_position + jump < len(houses):
        cupid_position += jump
    else:
        cupid_position = 0
    if houses[cupid_position] == 0:
        print(f'Place {cupid_position} already had Valentine\'s day.')
        command = input().split()
        continue
    houses[cupid_position] -= 2
    if houses[cupid_position] == 0:
        print(f'Place {cupid_position} has Valentine\'s day.')
    command = input().split()
print(f'Cupid\'s last position was {cupid_position}.')
for house in houses:
    if house != 0:
        count += 1
if count == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {count} places.')
