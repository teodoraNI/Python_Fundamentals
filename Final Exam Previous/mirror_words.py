import re

text = input()
mirror_words = []
pattern_word_pairs = r'(#|@)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
word_pairs = re.findall(pattern_word_pairs, text)
if word_pairs != []:
    print(f'{len(word_pairs)} word pairs found!')
    for group in word_pairs:
        if group[1] == group[2][::-1]:
            mirror_words.append(f'{group[1]} <=> {group[2]}')
else:
    print('No word pairs found!')
if mirror_words != []:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print('No mirror words!')



