food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
guineas_weight  = float(input()) * 1000
something_finished = False

for i in range(1,31):
    food -= 300
    if i%2 == 0:
        hay -= food*0.05
    if i%3 == 0:
        cover -= guineas_weight/3
    if food <= 0 or hay <= 0 or cover <= 0:
        print('Merry must go to the pet store!')
        something_finished = True
        break
if not something_finished:
    print(f'Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.')


