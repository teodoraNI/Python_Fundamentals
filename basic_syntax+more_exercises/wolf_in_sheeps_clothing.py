wolf_and_sheeps = input()
current_word = ""
counter_sheep = 0
if wolf_and_sheeps[len(wolf_and_sheeps)-1] == 'f':
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(wolf_and_sheeps) - 1, 0, -1):
        if wolf_and_sheeps[i] == ',':
            continue
        elif wolf_and_sheeps[i] == ' ':
            if current_word == 'sheep':
                counter_sheep += 1
                current_word = ""
                continue
            elif current_word == 'wolf':
                print(f"Oi! Sheep number {counter_sheep}! You are about to be eaten by a wolf!")
                break
        else:
            current_word = wolf_and_sheeps[i] + current_word


