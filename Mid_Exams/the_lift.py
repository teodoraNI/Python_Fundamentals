people_num = int(input())
lift_state = input()
lift_status = [int(x) for x in lift_state.split(' ')]

for i in range(len(lift_status)):
    if people_num - (4 - lift_status[i]) >= 0:
        people_num = people_num - (4 - lift_status[i])
        lift_status[i] = 4
        if people_num == 0 and lift_status[-1] == 4:
            print(*(lift_status)) #prints list members with whitespaces b/w and w/o []
    else:
        lift_status[i] += people_num
        people_num = 0
        print("The lift has empty spots!")
        print(*(lift_status))
        break
if people_num > 0:
    print(f"There isn't enough space! {people_num} people in a queue!")
    print(*(lift_status))
