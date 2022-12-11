def merge(lst, start_index, end_index):
    if end_index >= len(lst):
        end_index = len(lst) - 1
    if start_index < 0:
        start_index = 0
    if start_index < len(lst) - 1 and end_index > 0:
        merged = ''.join(lst[start_index:end_index + 1])
        for i in range(start_index, end_index + 1):
            lst.pop(start_index)
        lst.insert(start_index, merged)
    return lst


def divide(lst, position, parts):
    divided_lst = []
    if len(lst[position]) / parts <= 1:
        divided_lst = lst[position]
    else:
        division = lst[position]
        for i in range(parts-1):
            divided_lst.append(division[0:len(lst[position]) // parts])
            division = division[len(lst[position]) // parts::]
        divided_lst.append(division[::])
    lst.pop(position)
    lst.insert(position, ' '.join(divided_lst))
    return lst


strings_lst = input().split()
command = input()
while command != '3:1':
    expanded = command.split()
    action = expanded[0]
    if action == 'merge':
        start = int(expanded[1])
        end = int(expanded[2])
        merge(strings_lst, start, end)
    elif action == 'divide':
        index = int(expanded[1])
        partitions = int(expanded[2])
        divide(strings_lst, index, partitions)
    command = input()
print(*strings_lst)