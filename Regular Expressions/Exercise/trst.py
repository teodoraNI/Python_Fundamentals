import re

pattern = r'(blue|white|red)'
text = 'blue socks and red shoes'
new_text = re.subn(pattern, 'color', text, 1)
print(new_text)
