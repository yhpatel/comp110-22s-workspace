"""Tests for the Dictionary Program."""

__author__ = "730463236"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


"""This tests the invert function."""


def test_invert_edge() -> None:
    """This is an edge test for the invert function for an empty dictionary."""
    a: dict[str, str] = dict()
    assert invert(a) == {}


def test_invert_small() -> None:
    """This is a unit test for the invert function with a small inputted dictionary."""
    a: dict[str, str] = {"a": "hi", "b": "bye"}
    assert invert(a) == {"hi": "a", "bye": "b"}


def test_invert_big() -> None: 
    """This is a unit test for the invert function with a large inputted dictionary."""
    a: dict[str, str] = {"Elon": "cool", "Starlink": "crazy", "Plane": "Starship", "Race": "Racecar"}
    assert invert(a) == {"cool": "Elon", "crazy": "Starlink", "Starship": "Plane", "Racecar": "Race"}


"""This tests the favorite_color function."""


def test_favorite_color_edge() -> None:
    """This is an edge test for the favorite_color function for an empty dicitionary."""
    a: dict[str, str] = dict()
    assert favorite_color(a) == ""


def test_favorite_color_small() -> None: 
    """This is a unit test for the favorite_color function with a small inputted dictionary."""
    a: dict[str, str] = {"Bob": "green", "jj": "green", "Rocky": "blue", "reese": "green", "Speed": "blue"}
    assert favorite_color(a) == "green"


def test_favorite_color_large() -> None:
    """This is a unit test for teh favorite_color function with a large inputted dictionary."""
    a: dict[str, str] = {"McQueen": "blue", "John": "green", "Ronald": "blue", "Emma": "yellow", "Yash": "purple", "Brady": "blue"}
    assert favorite_color(a) == "blue"


"""This tests the count function."""


def test_count_edge() -> None:
    """This is an edge test for the count function with an empty list."""
    alist: list[str] = []
    assert count(alist) == {}


def test_count_small() -> None:
    """This is a unit test for the count function with a small inputted list."""
    alist: list[str] = ["Yash", "Yash", "Bob", "Bob"]
    assert count(alist) == {"Yash": 2, "Bob": 2}


def test_count_large() -> None:
    """This is a unit test for the count function with a large inputted list."""
    alist: list[str] = ["Race", "Baseball", "Race", "Boat", "Float", "Paint", "Baseball", "Baseball", "Float"]
    assert count(alist) == {"Race": 2, "Baseball": 3, "Boat": 1, "Float": 2, "Paint": 1}