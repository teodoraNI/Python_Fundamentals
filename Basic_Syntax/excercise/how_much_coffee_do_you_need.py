total_coffees = 0
command = ""
while command != "END":
    command = input()
    if (command.lower()) == "coding" or (command.lower()) == "cat" or (command.lower()) == "dog" or (command.lower()) == "movie":
        if command.islower():
            total_coffees +=1
        elif command.isupper():
            total_coffees += 2
if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)
