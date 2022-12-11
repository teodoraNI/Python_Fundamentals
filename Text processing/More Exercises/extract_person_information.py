n = int(input())
name = ''
age = ''
for i in range(0,n):
    string = input()
    for j in range(len(string)):
        if string[j] == '@':
            start_index_name = j+1
        elif string[j] == '|':
            end_index_name = j
        elif string[j] == ('#'):
            start_index_age = j+1
        elif string[j] == ('*'):
            end_index_age = j
    name = string[start_index_name:end_index_name]
    age = string[start_index_age:end_index_age]
    print(f"{name} is {age} years old.")
