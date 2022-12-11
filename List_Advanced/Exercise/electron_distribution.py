electrons = int(input())
shells = []
i = 1
while electrons > 0:
    if electrons >= 2*i*i:
        electrons -= 2*i*i;
        shells.append(2*i*i)
        i += 1
    else:
        shells.append(electrons)
        break
print(shells)