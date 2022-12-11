population = [int(x) for x in input().split(', ')]
min_wealth = int(input())
equality_is_utopia = False
for i in range(len(population)):
    if population[i] < min_wealth:
        gap_wealth = min_wealth - population[i]
        if max(population) - gap_wealth < min_wealth:
            print("No equal distribution possible")
            equality_is_utopia = True
            break
        else:
            index_max = population.index(max(population))
            population[index_max] -= gap_wealth
            population[i] += gap_wealth
if equality_is_utopia == False:
    print(population)
