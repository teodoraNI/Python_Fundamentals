number_of_people = int(input()) #17
elevators_capacity = int(input()) #3
if number_of_people % elevators_capacity == 0:
    needed_courses = number_of_people / elevators_capacity
else:
    needed_courses = number_of_people // elevators_capacity + 1
print(needed_courses)