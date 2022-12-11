string_one = input()
string_two = input()
last_printed_string = string_one
for index in range(len(string_two)):
    left_part = string_two[:index+1]
    right_part = string_one[index+1:]
    new_string = left_part + right_part
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string