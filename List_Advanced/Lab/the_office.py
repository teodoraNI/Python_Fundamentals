employees_happiness = list(map(int, input().split()))
useless = input()
average_happiness = sum(employees_happiness) / len(employees_happiness)
happy = [employee for employee in employees_happiness if employee >= average_happiness]
if len(happy) >= len(employees_happiness)/2:
    print(f'Score: {len(happy)}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy)}/{len(employees_happiness)}. Employees are not happy!')

