string1, string2 = input(). split()
sum = 0
if len(string1) >= len(string2):
    longer_str = string1
    shorter_str = string2
else:
    longer_str = string2
    shorter_str = string1
for i in range(len(shorter_str)):
    sum += ord(shorter_str[i]) * ord(longer_str[i])
for j in range(len(longer_str[len(shorter_str):])):
    sum += ord(longer_str[len(shorter_str) + j])
print(sum)

