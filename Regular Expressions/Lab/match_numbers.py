import re

text = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))'
results = re.finditer(pattern, text)
for result in results:
    print(result.group(), end = ' ')
