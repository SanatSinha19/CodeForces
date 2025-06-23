table_card = input().strip()
hand_cards = input().strip().split()

table_rank = table_card[0]
table_suit = table_card[1]

for card in hand_cards:
    if card[0] == table_rank or card[1] == table_suit:
        print("YES")
        break
else:
    print("NO")
