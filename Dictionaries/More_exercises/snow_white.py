# dwarfs = {}
# while True:
#     command = input()
#     if command == "Once upon a time":
#         break
#     name, color, physics = command.split(' <:> ')
#     if (name, color) not in dwarfs.keys():
#         dwarfs[(name, color)] = int(physics)
#     else:
#         if dwarfs[(name, color)] < int(physics):
#             dwarfs[(name, color)] = int(physics)
#
# sorted_by_physics = dict(sorted(dwarfs.items(), key=lambda x: (x[1], x[0][1]), reverse=True))
# sorted__by_hat_color = dict(sorted(sorted_by_physics.items(), key=lambda x: x[0][1], reverse=True))
#
# for key, value in sorted_by_physics.items():
#     print(f"({key[1]}) {key[0]} <-> {value}")

dwarfs = {}
while True:
    command = input()
    if command == "Once upon a time":
        break
    name, color, physics = command.split(' <:> ')
    if color not in dwarfs.keys():
        dwarfs[color] = [[int(physics), name]]
    else:
        name_exists = False
        for value in dwarfs[color]:
            if name in value:
                name_exists = True
                if int(value[0]) < int(physics):
                    value[0] = int(physics)
                    break
        if name_exists == False:
            dwarfs[color] += [[int(physics), name]]
sorted_dwarfs_by_color_occurrence = dict(sorted(dwarfs.items(), key=lambda x: len(x[1]), reverse=True))
new_list = []
for key in sorted_dwarfs_by_color_occurrence.keys():
    for value in sorted_dwarfs_by_color_occurrence[key]:
        new_list.append((value[1], key, value[0]))
sorted_result = sorted(new_list, key=lambda x: x[2], reverse=True)
for list in sorted_result:
    print(f"({list[1]}) {list[0]} <-> {list[2]}")




