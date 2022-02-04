import re
from typing import Counter, DefaultDict

# pawn scores contains the number of pawns and their scores
# this is a counter of the score with the number of pawns as value
PawnScores = Counter[int]

# a position is a location on the board and contains pawns with scores.
# a positions dict contains all positions for a player on the board annd their pawns and scores
Positions = DefaultDict[int, PawnScores]

# player poistions is a dict of players and their player_positions on the board
Player_Positions = DefaultDict[int, Positions]


def any_position_still_in_play(player_positions: Player_Positions) -> bool:
    return any(
        len(pawn_scores) > 0
        for pawn_scores in [
            positions.values() for positions in player_positions.values()
        ]
    )


# fget starting player_positions
player_positions = Player_Positions()
for line in open("input_21.txt"):
    stripped_line = line.strip()
    m = re.match(r"Player (\d+) starting position: (\d+)", stripped_line)
    player_positions[int(m.group(1))] = {int(m.group(2)): Counter({0: 1})}
    # player_positions[player][position] = {score: occurrences}

# dict of games won per player
games_won = {k: 0 for k in player_positions}

# when throwing a die three times, these are the odds of th eoutcome
die_odds = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

turns = 0
while any_position_still_in_play(player_positions):
    turns += 1

    # for each player
    for player, positions in player_positions.items():
        old_positions = positions.copy()
        for old_board_position, old_pawn_scores in old_positions.items():
            del positions[old_board_position]

            for old_score, old_pawns in old_pawn_scores.items():

                for die_result, odds in die_odds.items():
                    new_board_position = (old_board_position + die_result - 1) % 10 + 1
                    new_score = old_score + new_board_position
                    new_pawns = old_pawns * odds
                    if new_score >= 21:
                        games_won[player] += new_pawns
                        continue

                    pawn_score = positions.get(new_board_position, Counter())
                    pawn_score[new_score] += new_pawns
                    positions[new_board_position] = pawn_score

        num_pawns = sum(
            [sum(pawn_scores.values()) for pawn_scores in positions.values()]
        )
        print(f"turn {turns} - player {player} - {num_pawns} - won {games_won[player]}")

print(games_won)
