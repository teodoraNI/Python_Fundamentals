cards = input().split()
shuffles = int(input())
current_cards = []
for _ in range(shuffles):
    cards1 = cards[:len(cards)//2]
    cards2 = cards[len(cards)//2:]
    current_cards = []
    for i in range(len(cards)//2):
        current_cards.append(cards1[i])
        current_cards.append(cards2[i])
    cards = current_cards
print(cards)


