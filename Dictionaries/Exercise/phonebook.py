phonebook = {}
info = input().split('-')
while len(info) > 1:
    name, phone = info[0], info[1]
    phonebook[name] = phone
    info = input().split('-')
n = int(info[0])
for _ in range(n):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")




