companies_data = {}
while True:
    command = input()
    if command == 'End':
        break
    company, employee = command.split(' -> ')
    if company not in companies_data.keys():
        companies_data[company] = []
    if employee not in companies_data[company]:
        companies_data[company].append(employee)
for company, employees in companies_data.items():
    print(f"{company}")
    for item in companies_data[company]:
        print(f"-- {item}")



