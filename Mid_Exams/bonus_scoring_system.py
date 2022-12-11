from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendances = 0
for student in range(students):
    attendances = int(input())
    total_bonus = ceil(attendances / lectures * (5 + additional_bonus))
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendances = attendances
print(f'Max Bonus: {max_bonus}.\nThe student has attended {max_attendances} lectures.')