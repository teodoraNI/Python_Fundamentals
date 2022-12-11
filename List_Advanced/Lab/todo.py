todo_list = []
while True:
    command = input()
    if command == 'End':
        break
    todo = command.split('-')
    importance, task = int(todo[0]), todo[1]
    todo_list.append([importance,task])
sorted_todo_list = [task[1] for task in sorted(todo_list)]
print(sorted_todo_list)
