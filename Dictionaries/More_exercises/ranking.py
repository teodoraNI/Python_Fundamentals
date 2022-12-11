contests = {}
users = {}
while True:
    command = input()
    if command == 'end of contests':
        continue
    elif command == 'end of submissions':
        break
    elif ':' in command:
        contest, password = command.split(":")
        contests[contest] = password
    elif '=>' in command:
        contest, password, username, points = command.split('=>')
        if contest in contests.keys() and contests[contest] == password:
            if username not in users.keys():
                users[username] = {}
            if contest not in users[username].keys():
                users[username][contest] = 0
            if users[username][contest] < int(points):
                users[username][contest] = int(points)
max_points = 0
best_user = ""
for username in users.keys():
    total_points = sum(users[username].values())
    if total_points > max_points:
        max_points = total_points
        best_user = username
print(f"Best candidate is {best_user} with total {max_points} points.")
print("Ranking:")
for user in sorted(users.keys(), key=lambda x: x[0]):
    print(f"{user}")
    for contest, points in sorted(users[user].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {points}")



