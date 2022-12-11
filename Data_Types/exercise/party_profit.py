group_size = int(input())
days = int(input())
coins = 0
for day in range(1, days+1):
    coins += 50
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    coins -= group_size * 2
    if day % 3 == 0:
        coins -= group_size * 3
    if day % 5 == 0:
        coins += group_size * 20
        if day % 3 == 0:
            coins -= group_size * 2
print(f"{group_size} companions received {int(coins/group_size)} coins each.")