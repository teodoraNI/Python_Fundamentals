string = input()
dict_chars = dict()
for i in range(len(string)):
    if string[i] == ' ':
        continue
    if string[i] not in dict_chars.keys():
        dict_chars[string[i]] = 0
    dict_chars[string[i]] +=1
for char, value in dict_chars.items():
    print(f"{char} -> {value}")