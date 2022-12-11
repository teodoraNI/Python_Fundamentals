import re

all_places = input()
travel_points = 0
valid_destinations = []
matches = re.finditer(r'(\/|=)([A-Z][a-zA-Z]{2,})\1', all_places)
if matches:
    for match in matches:
        valid_destinations.append(match.group(2))
for destination in valid_destinations:
    travel_points += len(destination)
print(f'Destinations: {", ".join(valid_destinations)}')
print(f'Travel Points: {travel_points}')