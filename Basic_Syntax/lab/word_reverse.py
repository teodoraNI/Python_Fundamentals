word = input()
reversed_word = " "
for i in range((len(word) - 1), -1, -1):
    reversed_word += word[i]
print(reversed_word)


# word = input()
# a = - len(word)
# print(word[slice(-1, a -1, -1)])