courses = {}
data = input().split(":")
while len(data) > 1:
    name, id, course = data[0], data[1], data[2]
    if course not in courses:
        courses[course] = []
    courses[course].append(name+" - "+id)
    data = input().split(":")
course_for_statistic = data[0].replace("_", " ")
print(*courses[course_for_statistic], sep = '\n')
