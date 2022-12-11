languages = {}
students = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    data = command.split('-')
    username = data[0]
    if data[1] == 'banned':
        students.pop(username)
        continue
    language = data[1]
    points = int(data[2])
    if username not in students.keys():
        students[username] = 0
    if students[username] < points:
        students[username] = points
    if language not in languages.keys():
        languages[language] = 0
    languages[language] += 1
print("Results:")
for username, points in students.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, value in languages.items():
    print(f"{language} - {value}")

