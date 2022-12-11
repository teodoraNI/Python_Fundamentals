people = input().split()
k = int(input())
people_list = [int(people[i]) for i in range(len(people))]
a = len(people_list)
executed = []
counter = 0
indexes = []
while len(people_list) != 0:
    for j in range(len(indexes)):
        people_list.pop(indexes[j] - j)
    indexes = []
    a = len(people_list)
    for i in range(1, a + 1):
        counter +=1
        if counter == k:
            executed.append(people_list[i-1])
            indexes.append(i-1)
            counter = 0
        if i == a:
            i = 0
print('[', end='')
print(*executed, sep=',', end='')
print(']')
