num1 = int(input())
num2 = int(input())
num3 = int(input())
first_num = int(input())
step_num = int(input())
common_num_found = False

list_tribonachi =[num1, num2, num3]
while True:
    new_member = list_tribonachi[-1] + list_tribonachi[-2] + list_tribonachi[-3]
    if new_member > 1000000:
        break
    list_tribonachi.append(new_member)

number_row = [first_num]
spiral_count = 0
spiral_step_mul = 1
while True:
    new_member = number_row[-1] + step_num * spiral_step_mul
    if new_member > 1000000:
        break
    number_row.append(new_member)
    spiral_count += 1
    if spiral_count % 2 == 0:
        spiral_step_mul += 1
        
for k in range(len(list_tribonachi)):
    for m in range(len(number_row)):
        if list_tribonachi[k] == number_row[m]:
            common_num_found = True
            print(list_tribonachi[k])
            break
    if common_num_found:
        break
if common_num_found == False:
    print("No")