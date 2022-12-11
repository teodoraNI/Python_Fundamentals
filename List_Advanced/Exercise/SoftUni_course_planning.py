courses = input().split(', ')
command = input()
while command != 'course start':
    order = command.split(':')
    action, title = order[0], order[1]
    if action == 'Add':
        if title not in courses:
            courses.append(title)
    elif action == 'Insert':
        index = int(order[2])
        if title not in courses and 0 <= index < len(courses):
            courses.insert(index, title)
    elif action == 'Remove':
        while title in courses:
            courses.remove(title)
    elif action == 'Exercise':
        if title in courses and f'{title}-Exercise' not in courses:
            for i in range(courses.count(title)):
                courses.insert(courses.index(title) + 1, f'{title}-Exercise')
        elif title not in courses:
            courses.append(title)
            courses.append(f'{title}-Exercise')
    elif action == 'Swap':
        lesson = order[2]
        if title in courses and lesson in courses:
            ind1 = courses.index(title)
            ind2= courses.index(lesson)
            courses[ind1], courses[ind2] = courses[ind2], courses[ind1]
            if ind1 + 1 < len(courses) and ind2+1 < len(courses):
                if 'Exercise' in courses[ind1+1] and 'Exercise' in courses[ind2+1]:
                    courses[ind1+1], courses[ind2+1] = courses[ind2+1], courses[ind1+1]
            if ind1 + 1 < len(courses) and 'Exercise' in courses[ind1+1]:
                courses.insert(ind2+1, courses.pop(ind1+1))
            elif ind2 + 1 < len(courses) and 'Exercise' in courses[ind2 + 1]:
                courses.insert(ind1+1, courses.pop(ind2+1))
    command = input()
for count, course in enumerate(courses, 1):
    print(f'{count}.{course}')




