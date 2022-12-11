force_sides = {}
users = []
while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if '->' in command:
        force_user, force_side = command.split(' -> ')
        if force_side not in force_sides.keys() and force_user not in users:
            force_sides[force_side] = [force_user]
            users.append(force_user)
        elif force_user not in users:
            force_sides[force_side].append(force_user)
            users.append(force_user)
        elif force_user in users:
            for value in force_sides.values():
                if force_user in value:
                    value.remove(force_sides)
            force_sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    else:
        force_side, force_user = command.split(' | ')
        if force_side not in force_sides.keys() and force_user not in users:
            force_sides[force_side] = [force_user]
            users.append(force_user)
        elif force_user in users:
            continue
        elif force_user not in users:
            force_sides[force_side].append(force_user)
            users.append(force_user)
for force_side, force_user in force_sides.items():
    if len(force_sides[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_sides[force_side])}")
        [print(f"! {user}") for user in force_sides[force_side]]




