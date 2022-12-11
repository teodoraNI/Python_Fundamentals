lines = int(input())
new_str = ''
for i in range(lines):
    line = input()
    if line == '(' or line == ')':
        new_str = new_str + line
for j in range((len(new_str)-1)):
    if new_str[0] == ')' or new_str[-1] == '(':
        print("UNBALANCED")
        break
    if new_str[j] == new_str[j+1]:
        print("UNBALANCED")
        break
else:
    print("BALANCED")