"""Unit tests for list utility functions!"""

__author__ = "730573287"

from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests only_evens to see that given an empty list, only_evens returns an empty list."""
    assert only_evens([]) == []


def test_only_evens_many() -> None:
    """Tests only_evens to see that given a list of positive integers, the even ones are chosen."""
    ints: list[int] = [0, 1, 2, 3, 4, 5, 6]
    assert only_evens(ints) == [0, 2, 4, 6]


def test_only_evens_negative() -> None:
    """Tests only_evens to see that even if numbers in the list are negative, they are still correctly chosen as even numbers."""
    ints: list[int] = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    assert only_evens(ints) == [-4, -2, 0, 2, 4]


def test_concat_empty() -> None:
    """Tests concat to see that given two empty sets, an empty set is returned."""
    list_a: list[int] = []
    list_b: list[int] = []
    assert concat(list_a, list_b) == []


def test_concat_many() -> None:
    """Tests concat to see that given two sets, all elements of the second are added to a new list after all elements of the first."""
    list_a: list[int] = [1, 2, 50, 723, 5]
    list_b: list[int] = [4, 6, 7, 8, 9]
    assert concat(list_a, list_b) == [1, 2, 50, 723, 5, 4, 6, 7, 8, 9]


def test_concat_dif_lengths() -> None:
    """Tests concat to see that all elements of both lists are added to a new list despite difference in list length."""
    list_a: list[int] = [-2]
    list_b: list[int] = [1, 2, 3, 4, 5]
    assert concat(list_a, list_b) == [-2, 1, 2, 3, 4, 5]


def test_sub_empty() -> None:
    """Tests sub to see that an empty set is returned when given an empty set."""
    ints: list[int] = []
    assert sub(ints, 0, 1) == []


def test_sub_wrongly_indexed() -> None:
    """Tests sub to see that a start_index less than 0 will default to the first element of the list and a stop_index larger than the length of the list defaults to the last element of the list."""
    ints: list[int] = [1, 2, 3, 4]
    assert sub(ints, -1, 5) == [1, 2, 3, 4]


def test_sub_many() -> None:
    """Tests sub to see that an accurate subset of the list is made with all elements between start_index and stop_index-1."""
    ints: list[int] = [1, 2, 4, 5, 7, 8]
    assert sub(ints, 2, 5) == [4, 5, 7]