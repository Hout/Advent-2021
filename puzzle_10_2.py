from functools import reduce
from statistics import median


class Token:
    def __init__(self, c_in: str, c_out: str, penalty: int):
        self.c_in = c_in
        self.c_out = c_out
        self.penalty = penalty


TOKENS = [
    Token("(", ")", 1),
    Token("[", "]", 2),
    Token("{", "}", 3),
    Token("<", ">", 4),
]

IN_TOKENS = {t.c_in: t for t in TOKENS}
OUT_TOKENS = {t.c_out: t for t in TOKENS}


def find_mismatch(s: str) -> int:
    print(f"Processing {s}")
    stack = []
    for c in s:
        if c in IN_TOKENS:
            stack.append(IN_TOKENS[c])
            continue

        assert c in OUT_TOKENS

        expected_token = stack.pop()
        if c != expected_token.c_out:
            print("Corrupt line, ignored")
            return 0

    if stack != []:
        print(f"Incomlete, expected {''.join([t.c_out for t in reversed(stack)])}")
        return reduce(lambda p, c: p * 5 + c, [t.penalty for t in reversed(stack)])

    print("No issues")
    return 0


scores = []
for line in open("input_10.txt"):
    stripped_line = line.strip()
    error_score = find_mismatch(stripped_line)
    print(error_score, line)
    if error_score > 0:
        scores.append(error_score)


scores.sort()
print(scores)
print(scores[len(scores) // 2])
