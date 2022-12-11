dict_synonyms = dict()
n = int(input())
for _ in range(n):
    word = input()
    synonym = input()
    if word not in dict_synonyms.keys():
        dict_synonyms[word] = []
    dict_synonyms[word].append(synonym)
for word,synonyms in dict_synonyms.items():
    print(f"{word} - {', '.join(dict_synonyms[word])}")

