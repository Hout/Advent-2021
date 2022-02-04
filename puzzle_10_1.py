class Token:
    def __init__(self, c_in: str, c_out: str, penalty: int):
        self.c_in = c_in
        self.c_out = c_out
        self.penalty = penalty


TOKENS = [
    Token("(", ")", 3),
    Token("[", "]", 57),
    Token("{", "}", 1197),
    Token("<", ">", 25137),
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
            found_token = OUT_TOKENS[c]
            print(
                f"Expected token {expected_token.c_out}, found {c}, penalty {found_token.penalty}"
            )
            return found_token.penalty

    if stack != []:
        print("Incomlete, ignored")
        return 0

    print("No issues")
    return 0


total_error_score = 0
for line in open("input_10.txt"):
    stripped_line = line.strip()
    error_score = find_mismatch(stripped_line)
    print(error_score, line)
    total_error_score += error_score

print(total_error_score)
