"""List utility functions!"""

__author__ = "730573287"


def all(ints_list: list[int], num: int) -> bool:
    """This function returns true if every number in ints_list matches num, and false if even one element does not match num."""
    list_len: int = len(ints_list)
    index: int = 0

    if list_len == 0:
        return False

    while index < list_len:
        if ints_list[index] != num:
            return False
        else:
            index += 1
    
    return True


def max(ints_list: list[int]) -> int:
    """This function returns the largest integer of a list."""
    list_len: int = len(ints_list)
    index: int = 0
    current_max: int = ints_list[0]

    if list_len == 0:
        raise ValueError("max() arg is an empty List")
    
    while index < list_len:
        if ints_list[index] > current_max:
            current_max = ints_list[index]
        
        index += 1

    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function returns true if list1 and list2 are the exact same, and false if even one element differs."""
    list1_len: int = len(list1)
    list2_len: int = len(list2)
    index: int = 0

    if list1_len != list2_len:
        return False
    
    while index < list1_len:
        if list1[index] != list2[index]:
            return False
        
        index += 1

    return True