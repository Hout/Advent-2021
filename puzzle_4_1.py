import numpy as np

CARD_SIZE = 5

lines = [line.strip() for line in open("input_4.txt").readlines() if line != "\n"]

numbers = [int(s) for s in lines.pop(0).split(",")]

assert len(lines) % CARD_SIZE == 0

cards = []
for i in range(0, len(lines), CARD_SIZE):
    card = []
    for j in range(i, i + CARD_SIZE):
        card.append([int(s) for s in lines[j].split()])
    cards.append(card)

cards_matrix = np.array(cards)
for i in range(CARD_SIZE, len(numbers)):
    numbers_called = np.array(numbers[:i])
    for card in cards_matrix:
        for row in card:
            if np.all(np.isin(row, numbers_called)):
                # bingo!
                mask = np.isin(card, numbers_called)
                card_sum = np.sum(card[~mask])
                result = card_sum * numbers_called[-1]
                print(result)
                exit()
        for col in card.T:
            if np.all(np.isin(col, numbers_called)):
                # bingo!
                # bingo!
                mask = np.isin(card, numbers_called)
                card_sum = np.sum(card[~mask])
                result = card_sum * numbers_called[-1]
                print(result)
                exit()


print("no result")
