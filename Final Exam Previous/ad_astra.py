import re

text = input()
pattern = r'(#|\|)([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1'
result = []
total_calories = 0
matches = re.finditer(pattern, text)
for match in matches:
    result.append(f'Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}\n')
    total_calories += int(match.group(4))
days = int(total_calories / 2000)
print(f'You have food to last you for: {days} days!')
print(*result)