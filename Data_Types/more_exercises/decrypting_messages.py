key = int(input())
lines = int(input())
word = ''
for i in range(lines):
    letter = input()
    word = word + chr(ord(letter) + key)
print(word)