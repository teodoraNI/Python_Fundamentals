fires = input(). split('#')
water = int(input())
effort = 0
total_fire = 0
put_out_cells = []
for fire in fires:
    fire = fire.split(' = ')
    if fire[0] == 'High' and 81 <= int(fire[1]) <= 125 and water >= int(fire[1])\
        or fire[0] == 'Medium' and 51 <= int(fire[1]) <= 80 and water >= int(fire[1])\
        or fire[0] =='Low' and 1 <= int(fire[1]) <= 50 and water >= int(fire[1]):
        water -= int(fire[1])
        effort += int(fire[1]) * 0.25
        total_fire += int(fire[1])
        put_out_cells.append(int(fire[1]))
        if water == 0:
            break
print("Cells:")
for i in range(len(put_out_cells)):
    print(f" - {put_out_cells[i]}")
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")
