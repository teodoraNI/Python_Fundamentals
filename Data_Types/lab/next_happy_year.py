year = int(input())
it_is_happy_year = False
while not it_is_happy_year:
    year += 1
    year_set = set()
    for i in range(len(str(year))):
        year_set.add(str(year)[i])
    it_is_happy_year = len(str(year)) == len(year_set)
print(year)