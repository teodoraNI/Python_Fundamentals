# contests = {}
# users = {}
# while True:
#     command = input()
#     if command == "no more time":
#         break
#     username, contest, points = command.split(" -> ")
#     if contest not in contests:
#         contests[contest] = {}
#     if username not in contests[contest]:
#         contests[contest][username] = int(points)
#     if  contests[contest][username] < int(points):
#         contests[contest][username] = int(points)
#     if username not in users:
#         users[username] = {}
#     if contest not in users[username]:
#         users[username][contest] = int(points)
#     if users[username][contest] < int(points):
#         users[username][contest] = int(points)
# for contest in contests.keys():
#     print(f"{contest}: {len(contests[contest].keys())} participants")
#     for i, (username, points) in enumerate(sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])), 1):
#         print(f"{i}. {username} <::> {points}")
# print("Individual standings:")
# dict_indiv_standing = {}
# for username, contest in users.items():
#     total_points = 0
#     for contest in users[username]:
#         total_points += users[username][contest]
#     dict_indiv_standing.update({username:total_points})
# for i, (key, value) in enumerate(sorted(dict_indiv_standing.items(), key=lambda x: (-x[1], x[0])), 1):
#     print(f"{i}. {key} -> {value}")

contests = {}
while True:
    command = input()
    if command == "no more time":
        break
    student, contest, points = command.split(" -> ")
    if contest not in contests:
        contests[contest] = {}
    if student not in contests[contest].keys() or contests[contest][student] < int(points):
        contests[contest][student] = int(points)
for contest in contests.keys():
    print(f"{contest}: {len(contests[contest].keys())} participants")
    for i, (student, points) in enumerate(sorted(contests[contest].items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{i}. {student} <::> {points}")
print("Individual standings:")
students = {}
for contest in contests.keys():
    for student in contests[contest].keys():
        if student in students.keys() and (contest not in students[student].keys() or students[student][contest]<contests[contest][student]):
            students[student].update({contest:contests[contest][student]})
        else:
            students.update({student:{contest:contests[contest][student]}})
individual_scores = {student:sum(students[student].values()) for student in students}
for i, (student, points) in enumerate(sorted(individual_scores.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{i}. {student} -> {points}")

