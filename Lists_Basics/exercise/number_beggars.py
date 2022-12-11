charity = input().split(', ')
num_beggers = int(input())
money_per_begger = []
starting_index = 0
while len(money_per_begger) < num_beggers:
    begger_money = 0
    for i in range(starting_index, len(charity), + num_beggers):
       begger_money += int(charity[i])
    money_per_begger.append(begger_money)
    starting_index += 1
print(money_per_begger)

