employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
total_capacity = employee3_efficiency + employee2_efficiency + employee1_efficiency
students = int(input())
hours = 0
counter_hours_working = 0

while students > 0:
    students -= total_capacity
    hours += 1
    counter_hours_working += 1
    if counter_hours_working == 3 and students != 0:
        hours += 1
        counter_hours_working = 0
print(f"Time needed: {hours}h.")

