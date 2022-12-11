numbers = (input()).split(' ')
string = input()
final_string = ''

for m in range (len(numbers)):
    sum = 0
    new_number = int(numbers[m])
    while new_number > 0:
        sum += new_number % 10
        new_number = new_number // 10
    final_string = final_string + string[(sum % len(string))]
    string = string[:(sum % len(string))] + string[(sum % len(string))+1:]
print(final_string)