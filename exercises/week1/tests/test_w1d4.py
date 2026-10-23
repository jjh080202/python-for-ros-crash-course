import ast
import inspect

import pytest

from w1d4_loops import countdown, steps_until_low, sum_to


@pytest.mark.parametrize(
    "n, expected",
    [(3, "3 2 1 GO!"), (1, "1 GO!"), (0, "GO!"), (10, "10 9 8 7 6 5 4 3 2 1 GO!")],
)
def test_countdown(n, expected):
    assert countdown(n) == expected


@pytest.mark.parametrize("n, expected", [(4, 10), (0, 0), (1, 1), (100, 5050)])
def test_sum_to(n, expected):
    tree = ast.parse(inspect.getsource(sum_to))
    has_loop = any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))
    assert has_loop, "sum_to must add the numbers in a for or while loop, not with a formula or sum()"
    assert sum_to(n) == expected


@pytest.mark.parametrize(
    "battery, drain, low, expected",
    [(100, 10, 50, 5), (100, 7, 20, 12), (10, 5, 20, 0), (100, 1, 20, 80)],
)
def test_steps_until_low(battery, drain, low, expected):
    assert steps_until_low(battery, drain, low) == expected
