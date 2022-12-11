import re

dates = input()
pattern = r'\b(?P<day>\d{2})([-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'
results = re.finditer(pattern, dates)
for date in results:
    print(f'Day: {date.group("day")}, Month: {date.group("month")}, Year: {date.group("year")}')
