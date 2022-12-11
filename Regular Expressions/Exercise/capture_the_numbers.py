import re

line = input()
while line:
    pattern = r'\d+'
    result = re.findall(pattern, line)
    if result:
        print(' '.join(result), end=' ')
    line = input()
