"""Tests for util programs."""

from utils import only_evens
from utils import sub 
from utils import concat


"""Testing the only_evens function."""


def test_only_evens_empty() -> None:
    """Testing the only_evens function with an empty string."""
    num: list[int] = []
    assert only_evens(num) == []


def test_only_evens_less() -> None: 
    """Testing the only_evens function with a small string."""
    num: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(num) == [2, 4]


def test_only_evens_more() -> None:
    """Testing the only_evens function with a larger string."""
    num: list[int] = [2, 2, 4, 4, 6, 6, 8, 8]
    assert only_evens(num) == [2, 2, 4, 4, 6, 6, 8, 8]


"""Testing the sub function."""


def test_sub_empty() -> None: 
    """Testing the sub function with an empty string."""
    num: list[int] = []
    assert sub(num, 0, 5) == []


def test_sub_less() -> None: 
    """Testing the sub function with a small string."""
    num: list[int] = [5, 10, 15, 20, 25]
    assert sub(num, 2, 5) == [15, 20, 25]


def test_sub_more() -> None: 
    """Testing the sub function with a larger string."""
    num: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert sub(num, -1, 7) == [10, 20, 30, 40, 50, 60, 70]


"""Testing the concat function."""


def test_concat_empty() -> None:
    """Testing the concat function with an empty string."""
    num_evens: list[int] = [10, 15, 20]
    num_sub: list[int] = []
    assert concat(num_evens, num_sub) == [10, 15, 20]


def test_concat_less() -> None: 
    """Testing the concat function with a small string."""
    num_evens: list[int] = [1, 3, 4, 7]
    num_sub: list[int] = [3, 5, 6, 8]
    assert concat(num_evens, num_sub) == [1, 3, 4, 7, 3, 5, 6, 8]


def test_concat_more() -> None: 
    """Testing the concat function with a larger string."""
    num_evens: list[int] = [10, 20, 25, 30, 35, 50, 80]
    num_sub: list[int] = [5, 15, 32, 48, 65, 75, 95, 99, 100]
    assert concat(num_evens, num_sub) == [10, 20, 25, 30, 35, 50, 80, 5, 15, 32, 48, 65, 75, 95, 99, 100]