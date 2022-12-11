num_of_snowballs = int(input())
current_record = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
for i in range(num_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    score = (weight / time) ** quality
    if score > current_record:
        current_record = score
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality
print(f"{snowball_weight} : {snowball_time} = {int(current_record)} ({snowball_quality})")
