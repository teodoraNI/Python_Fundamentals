# my_dictionary = dict(name = "George", age = 18)
# print(my_dictionary) #{'name': 'George', 'age': 18}

bakery = {}
items = input().split()
for index in range(0, len(items), 2):
    food = items[index]
    quantity = int(items[index + 1])
    bakery[food] = quantity
print(bakery)


