initial_list = input().split(' ')
list = [int(initial_list[i]) for i in range(len(initial_list))]
list_odd = []
list_even = []
for i in range(len(list)):
    if list[i] % 2 != 0:
        list_odd.append(list[i])
    else:
        list_even.append(list[i])
command1 = input()
while command1 != 'end':
    command = command1.split()
    if command[0] == 'exchange':
        if int(command[1]) < 0 or int(command[1]) >= len(list):
            print("Invalid index")
        else:
            list1 = list[:(int(command[1]) + 1)]
            list2 = list[int(command[1])+1::]
            list = list2 + list1
    elif command[0] == 'max' and command[1] == 'even':
        if list_even == []:
            print("No matches")
        else:
            max_even = max(list_even)
            index_even_max = list.index(max_even)
            print(index_even_max)
    elif command[0] == 'max' and command[1] == 'odd':
        if list_odd == []:
            print("No matches")
        else:
            max_odd = max(list_odd)
            index_odd_max = list.index(max_odd)
            print(index_odd_max)
    elif command[0] == 'min' and command[1] == 'even':
        if list_even == []:
            print("No matches")
        else:
            min_even = min(list_even)
            index_even_min = list.index(min_even)
            print(index_even_min)
    elif command[0] == 'min' and command[1] == 'odd':
        if list_odd == []:
            print("No matches")
        else:
            min_odd = min(list_odd)
            index_odd_min = list.index(min_odd)
            print(index_odd_min)
    elif command[0] == 'first':
        if int(command[1]) > len(list):
            print("Invalid count")
            command1 = input()
            continue
        else:
            list_first_even = []
            list_first_odd = []
            for j in range(len(list)):
                if list[j] % 2 == 0 and len(list_first_even) < int(command[1]):
                    list_first_even.append(list[j])
                elif list[j] % 2 != 0 and len(list_first_odd) < int(command[1]):
                    list_first_odd.append(list[j])
            if command[2] == 'even':
                print(list_first_even)
            elif command[2] == 'odd':
                print(list_first_odd)
    elif command[0] == 'last':
        if int(command[1]) > len(list):
            print("Invalid count")
            command1 = input()
            continue
        else:
            list_last_even = []
            list_last_odd = []
            for j in range(-1, -(len(list)+1), -1):
                if list[j] % 2 == 0 and len(list_last_even) < int(command[1]):
                    list_last_even.append(list[j])
                elif list[j] % 2 != 0 and len(list_last_odd) < int(command[1]):
                    list_last_odd.append(list[j])
            if command[2] == 'even':
                list_last_even.reverse()
                print(list_last_even)
            elif command[2] == 'odd':
                list_last_odd.reverse()
                print(list_last_odd)
    command1 = input()
print(list)











