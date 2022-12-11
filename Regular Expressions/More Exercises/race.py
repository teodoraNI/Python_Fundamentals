import re

participants = input().split(', ')
distances = [0]
dictionary = {key:value for key in participants for value in distances}
while True:
    data = input()
    if data == 'end of race':
        break
    pattern_name = r'([A-Za-z]\w*?)'
    name = ''.join(re.findall(pattern_name, data))
    pattern_dist = r'([0-9]\w*?)'
    dist = sum(int(x) for x in re.findall(pattern_dist, data))
    if name in dictionary.keys():
        dictionary[name] += dist
final_results = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {final_results[0][0]}\n2nd place: {final_results[1][0]}\n3rd place: {final_results[2][0]}")