students = {}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[name] = []
    students[name].append(grade)
for name, grade in students.items():
    if sum(students[name]) / len(students[name]) >= 4.50:
        print(f"{name} -> {sum(students[name]) / len(students[name]):.2f}")



