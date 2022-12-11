number_of_commands = int(input())
parking = {}
for _ in range(number_of_commands):
    command = input().split(' ')
    action = command[0]
    username = command[1]
    if action == 'register':
        plate_num = command[2]
        if username not in parking.keys():
            parking[username] = plate_num
            print(f"{username} registered {parking[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")
    elif action == 'unregister':
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking.pop(username)
for username, plate_num in parking.items():
    print(f"{username} => {plate_num}")
