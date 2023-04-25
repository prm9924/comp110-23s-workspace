"""More list utility functions and unit testing!"""

__author__ = "730573287"


def only_evens(ints: list[int]) -> list[int]:
    """This function is given a list of ints and only returns the even ones."""
    even_ints: list[int] = []

    for num in ints:
        if num % 2 == 0:
            even_ints.append(num)

    return even_ints


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """This function takes two lists and creates a new list with the elements of both."""
    new_list: list[int] = []

    for num in list_a:
        new_list.append(num)   
    for num in list_b:
        new_list.append(num)

    return new_list


def sub(ints: list[int], start_index: int, stop_index: int) -> list[int]:
    """This function creates a subset of ints with the elements between the start and stop indices."""
    subset: list[int] = []

    if start_index < 0:
        start_index = 0
    if stop_index > len(ints):
        stop_index = len(ints)

    for i in range(start_index, stop_index):
        subset.append(ints[i])

    return subset