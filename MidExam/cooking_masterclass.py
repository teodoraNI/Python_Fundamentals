from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

total_costs = students * flour_price + students * 10 * egg_price + ceil(1.2 * students) * apron_price
free_flour_packs = students // 5
final_cost = total_costs - free_flour_packs * flour_price
if budget - final_cost >= 0:
    print(f'Items purchased for {final_cost:.2f}$.')
else:
    print(f'{final_cost - budget:.2f}$ more needed.')
