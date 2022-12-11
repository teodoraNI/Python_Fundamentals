def contains_substring(string, substring):
    if substring in string:
        return f"{string} contains {substring}"
    else:
        return "Substring not found!"

def flip_case(string, case, start_index, end_index):
    if case == "Upper":
        string = string[:start_index] + string[start_index:end_index].upper() + string[end_index:]
    elif case == "Lower":
        string = string[:start_index] + string[start_index:end_index].lower() + string[end_index:]
    return string

def delete(string, start_index, end_index):
    string = string[:start_index] + string[end_index:]
    return string

activation_key = input()
while True:
    command = input().split('>>>')
    if command[0] == "Generate":
        break
    elif command[0] == "Contains":
        print(contains_substring(activation_key, command[1]))
    elif command[0] == "Flip":
        activation_key = flip_case(activation_key, command[1], int(command[2]), int(command[3]))
        print(activation_key)
    elif command[0] == "Slice":
        activation_key = delete(activation_key, int(command[1]), int(command[2]))
        print(activation_key)
print(f"Your activation key is: {activation_key}")
