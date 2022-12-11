# import re

# string = "The rain in Spain!"
# a = re.search('\s', string)
# print(f"First occurance at {a.start()}")
import re
names = input()
pattern = r'\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b'
results = re.findall(pattern, names)
print(' '.join(results))