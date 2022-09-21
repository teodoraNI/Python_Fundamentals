while True:
    command = input()
    if command == "SoftUni":
        continue
    if command == "End":
        break
    for i in range(len(command)):
        print( 2 * command[i], end='')
    print()
