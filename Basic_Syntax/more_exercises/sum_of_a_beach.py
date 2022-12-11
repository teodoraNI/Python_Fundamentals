my_string = input().lower()
counter_water = my_string.count('water')
counter_fish = my_string.count('fish')
counter_sand = my_string.count('sand')
counter_sun = my_string.count('sun')
total_num_of_words = counter_sun+counter_fish+ counter_sand+ counter_water
print(total_num_of_words)
