from math import floor, ceil

input = (input()).split(' ')
time = [int(input[i]) for i in range(len(input))]
def time_calculation(x,y,z):
    time_car = 0
    for i in range(x,y,z):
        if time[i] != 0:
            time_car += time[i]
        else:
            time_car *= 0.8
    return(time_car)


result_left = time_calculation(0, floor(len(time) / 2), +1)
result_right = time_calculation(-1, -ceil(len(time)/2), -1)

if result_left > result_right:
    winner = 'right'
    total_time = result_right
else:
    winner = 'left'
    total_time = result_left
print(f"The winner is {winner} with total time: {total_time:.1f}")