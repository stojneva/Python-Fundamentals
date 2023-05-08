cards_deck = input().split()
number_shuffles = int(input())

for card in range(number_shuffles):
    deck = []
    middle_deck = len(cards_deck) // 2
    left = cards_deck[0: middle_deck]
    right = cards_deck[middle_deck::]
    for index in range(len(left)):
        deck.append(left[index])
        deck.append(right[index])
    cards_deck = deck
print(deck)

    

