pokemones = [int(x) for x in input().split()]
removed_sum = 0
while pokemones != []:
    index = int(input())
    if 0 <= index < len(pokemones):
        x = pokemones.pop(index)
    elif index < 0:
        x = pokemones.pop(0)
        pokemones.insert(index, pokemones[-1])
    elif index >= len(pokemones):
        x = pokemones.pop(-1)
        pokemones.insert(index, pokemones[0])
    removed_sum += x
    pokemones = list(map(lambda item: item + x if (item <= x) else item - x, pokemones))
print(removed_sum)
