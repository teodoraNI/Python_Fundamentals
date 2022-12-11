import re

text = input()
cool_threshold = 1
for char in text:
    if char.isdigit():
        cool_threshold *= int(char)
emojis = re.findall(r'[:]{2}[A-Z][a-z]{2,}[:]{2}|[*]{2}[A-Z][a-z]{2,}[*]{2}', text)
print(f"Cool threshold: {cool_threshold}\n{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in emojis:
    emoji_coolness = sum(ord(char) for char in emoji if char.isalpha())
    if emoji_coolness >= cool_threshold:
        print(emoji)

# import re
#
# string = "The rain in Spain!"
# a = re.search('\s', string)
# print(f"First occurance at {a.start()}")

