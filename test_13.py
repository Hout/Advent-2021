import puzzle_13_1

# import pytest


def test_folding():
    assert puzzle_13_1.fold_along("x", 1, [(2, 2)]) == [(0, 2)]
    assert puzzle_13_1.fold_along("y", 1, [(2, 2)]) == [(2, 0)]
