cars_number = int(input())
cars = {}
for _ in range(cars_number):
    car, mileage, fuel = input().split('|')
    cars[car] = [int(mileage), int(fuel)]
while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Drive':
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[car][1] < fuel:
            print('Not enough fuel to make that ride')
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car][0] >= 100000:
            print(f'Time to sell the {car}!')
            del cars[car]
    elif command[0] == 'Refuel':
        car, fuel = command[1], int(command[2])
        if cars[car][1] + fuel > 75:
            fuel = 75 - cars[car][1]
            cars[car][1] = 75
        else:
            cars[car][1] += fuel
        print(f'{car} refueled with {fuel} liters')
    elif command[0] == 'Revert':
        car, kilometers = command[1], int(command[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')
for car, data in cars.items():
    print(f'{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.')

