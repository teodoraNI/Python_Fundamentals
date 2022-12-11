rooms = int(input())
no_free_chairs = False
free_chairs = 0
for room in range(1, rooms+1):
    info = input().split(' ')
    chairs = len(info[0])
    visitors = int(info[1])
    if visitors > chairs:
        print(f'{visitors - chairs} more chairs needed in room {room}')
        no_free_chairs = True
    elif visitors < chairs:
        free_chairs += chairs - visitors
if not no_free_chairs:
    print(f'Game On, {free_chairs} free chairs left')

