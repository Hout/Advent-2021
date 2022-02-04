import numpy as np

CARD_SIZE = 5

lines = [line.strip() for line in open("input_4.txt").readlines() if line != "\n"]

numbers = [int(s) for s in lines.pop(0).split(",")]

assert len(lines) % CARD_SIZE == 0


def bingo(card, numbers_called):
    for row in card:
        if np.all(np.isin(row, numbers_called)):
            return True
    for col in card.T:
        if np.all(np.isin(col, numbers_called)):
            return True
    return False


cards = []
for i in range(0, len(lines), CARD_SIZE):
    card = []
    for j in range(i, i + CARD_SIZE):
        card.append([int(s) for s in lines[j].split()])
    cards.append(card)

cards_matrix = np.array(cards)
valid_cards = set(range(cards_matrix.shape[0]))
for i in range(CARD_SIZE, len(numbers)):
    numbers_called = np.array(numbers[:i])
    for card_index, card in enumerate(cards_matrix):
        if card_index not in valid_cards:
            continue

        if bingo(card, numbers_called):
            valid_cards.remove(card_index)

            if len(valid_cards) == 0:
                mask = np.isin(card, numbers_called)
                card_sum = np.sum(card[~mask])
                result = card_sum * numbers_called[-1]
                print(result)
                exit()

print("no result")
