n = int(input())
word = input()
list_strings = [''.join(input()) for _ in range(n)]
print(list_strings)
filtered_list = []
for i in range(len(list_strings)):
    if word in list_strings[i]:
        filtered_list.append(list_strings[i])
print(filtered_list)



