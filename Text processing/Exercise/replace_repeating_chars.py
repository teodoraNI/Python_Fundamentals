chars_list = list(input())
for i in range(len(chars_list)- 1):
    if chars_list[i] == chars_list[i+1]:
        chars_list[i] = ''
print(*chars_list, sep='')