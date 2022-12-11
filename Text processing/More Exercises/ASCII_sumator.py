start_ASCII = ord(input())
end_ASCII = ord(input())
random_string = input()
sum = 0
for char in random_string:
    if char.isdigit() and start_ASCII < int(char) < end_ASCII:
        sum += int(char)
    elif start_ASCII < ord(char) < end_ASCII:
        sum += ord(char)
print(sum)
