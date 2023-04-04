"""Unit tests for dictionary!"""

__author__ = "730573287"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty_dictionary() -> None:
    """Tests invert to see that an empty dictionary is returned when given an empty one."""
    assert invert({}) == {}


def test_invert_one() -> None:
    """Tests invert to see if a dictionary of length one is inverted."""
    my_dict: dict[str, str] = {"comp": "110"}
    assert invert(my_dict) == {"110": "comp"}


def test_invert_mulitple() -> None:
    """Tests invert to see if a dictionary of longers length is inverted."""
    my_dict: dict[str, str] = {"comp": "110", "stor": "215", "math": "232"}
    assert invert(my_dict) == {"110": "comp", "215": "stor", "232": "math"}


def test_largest_key_empty() -> None:
    """Tests largest key to see that nothing is returned when given an empty dictionary."""
    assert favorite_color({}) == "None"


def test_largest_key_no_tie() -> None:
    """Tests largest key when there are mulitple keys and no among between the most frequent colors."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_largest_key_with_tie() -> None:
    """Tests largest key when there is a tie among the most frequent colors."""
    assert favorite_color({"Ishaan": "blue", "Adi": "yellow", "Divij": "blue", "Ashrith": "blue", "Eren": "yellow", "Reiner": "yellow"}) == "blue"


def test_count_empty() -> None:
    """Tests count to see that an empty dictionary is returned when an empty list is given."""
    assert count([]) == {}


def test_count_one() -> None:
    """Tests count when there is only one key."""
    my_list: list[str] = ["red"]
    assert count(my_list) == {"red": 1}


def test_count_many() -> None:
    """Tests count when there are many keys."""
    my_list: list[str] = ["red", "green", "red", "yellow"]
    assert count(my_list) == {"red": 2, "green": 1, "yellow": 1}