"""Tests for codewars kata https://www.codewars.com/kata/best-travel/."""

import pytest

cities = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

TEST_INPUT = [
    (163, 3, cities, 163),
    (230, 4, cities, 230),
    (430, 5, cities, 430),
    (430, 8, cities, None),
]


@pytest.mark.parametrize('t, k, ls, result', TEST_INPUT)
def test_choose_best_sum(t, k, ls, result):
    """Test that for a list, function returns correct result."""
    from best_travel import choose_best_sum
    assert choose_best_sum(t, k, ls) == result
