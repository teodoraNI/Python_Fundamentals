import re

urls = []
line = input()
while line:
    pattern = r'(w{3}\.[A-Za-z0-9]+([\-A-Za-z0-9]+)*(\.[a-z]+)+)'
    match = re.search(pattern, line)
    if match and match not in urls:
        urls.append(match.group(0))
    line = input()
print('\n'.join(urls))

