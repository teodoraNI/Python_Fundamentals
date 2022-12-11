countries = input().split(', ')
capitals = input().split(', ')
dictionary = dict(zip(countries, capitals))
# dictionary = {countries[i]: capitals[i] for i in range(len(countries)}
for country, capital in dictionary.items():
    print(f"{country} -> {capital}")
