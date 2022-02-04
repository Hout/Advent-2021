import sys
import re


class Die:
    def __init__(self, max=None) -> None:
        self._max = max or 100
        self._last_outcome = 0
        self._throws = 0

    def throw(self) -> int:
        die_outcome = self._last_outcome % self._max + 1
        self._last_outcome = die_outcome
        self._throws += 1
        return die_outcome

    @property
    def throws(self):
        return self._throws


# fget starting positions
positions = dict()
for line in open("input_21.txt"):
    stripped_line = line.strip()
    m = re.match(r"Player (\d+) starting position: (\d+)", stripped_line)
    positions[int(m.group(1))] = int(m.group(2))

die = Die(max=100)
num_players = 2
max_score = 1000
die_rolls = 0
die_throws_per_turn = 3
scores = {k: 0 for k in positions}
board_size = 10


while True:
    for player in range(1, num_players + 1):
        # roll die 3 times
        for _ in range(die_throws_per_turn):
            steps = die.throw()
            new_position = (positions[player] + steps - 1) % board_size + 1
            positions[player] = new_position
        scores[player] += positions[player]
        if scores[player] >= max_score:
            # won!
            print(f"Player {player} won")
            print(f"Losers are {[p for p in positions if p != player]}")
            loser_points = sum([score for p, score in scores.items() if p != player])
            print(f"Losers have {loser_points} points")
            print(f"Die rolled {die.throws} times")
            print(f"Result = {loser_points*die.throws}")
            sys.exit()
