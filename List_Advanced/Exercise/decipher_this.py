words = input().split()
for i in range(len(words)):
    word = list(words[i])
    code = ''
    for j in range(len(word)):
        if word[0].isdigit():
            code += word.pop(0)
    word.insert(0,chr(int(code)))
    word[1], word[-1] = word[-1], word[1]
    words[i] = ''.join(word)
print(*words)
