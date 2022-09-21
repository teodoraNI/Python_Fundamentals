budget = int(input())
total_purchases = 0
command = input()
while command != "End":
    item_price = int(command)
    total_purchases += item_price
    if total_purchases > budget:
        print("You went in overdraft!")
        break
    command = input()
if command == "End":
    print("You bought everything needed.")