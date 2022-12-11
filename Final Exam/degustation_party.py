guests = {}
unliked_meals = []
while True:
    data = input().split('-')
    if data[0] == 'Stop':
        break
    command, guest, meal = data[0], data[1], data[2]
    if command == 'Like':
        if guest not in guests.keys():
            guests[guest] = [meal]
        else:
            if meal not in guests[guest]:
                guests[guest].append(meal)
    elif command == 'Dislike':
        if guest not in guests.keys():
            print(f"{guest} is not at the party.")
        else:
            if meal not in guests[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                guests[guest].remove(meal)
                unliked_meals.append(meal)
                print(f"{guest} doesn't like the {meal}.")
for guest, meals in guests.items():
    print(f"{guest}: {', '.join(guests[guest])}")
print(f"Unliked meals: {len(unliked_meals)}")
