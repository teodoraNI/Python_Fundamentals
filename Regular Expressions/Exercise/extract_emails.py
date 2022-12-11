import re

text = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'
results = re.findall(pattern, text)
for result in results:
    print(result[0])