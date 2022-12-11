courses = {}
command = input().split(' : ')
while command[0] != 'end':
    course = command[0]
    name = command[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
    command = input().split(' : ')
for course, names in courses.items():
    print(f"{course}: {len(courses[course])}")
    for name in names:
        print(f"-- {name}")




