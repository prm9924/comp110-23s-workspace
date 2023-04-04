"""Exercise 7 - Dictionary Functions!"""

__author__ = "730573287"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Swaps the positions of the original dictionary's keys and values."""
    inverted_dict: dict[str, str] = {}

    # checks to see if there are repeat values.
    values: str = list()
    for key in input_dict:
        values.append(input_dict[key])
    
    for item in values:
        count: int = 0
        for val in values:
            if item == val:
                count += 1
            if count > 1:
                raise KeyError("There are repeat values in the input dictionary.")

    # if there are no repeats, the dictionary is inverted.
    for key in input_dict:
        inverted_dict[input_dict[key]] = key
    
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the favorite color that appears the most in input dictionary."""
    if len(input_dict) == 0:
        return "None"
    
    values: str = list()
    for key in input_dict:
        values.append(input_dict[key])

    count_list: list[int] = []
    for item in values:
        count: int = 0
        for val in values:
            if item == val:
                count += 1
        count_list.append(count)

    dict_with_counts: dict[str, int] = {}
    idx: int = 0
    for key in input_dict:
        dict_with_counts[input_dict[key]] = count_list[idx]
        idx += 1

    largest: int = 0
    for key in dict_with_counts:
        if dict_with_counts[key] > largest:
            largest = dict_with_counts[key]
            largest_key: str = key
    
    return largest_key


def count(input_list: list[str]) -> dict[str, int]:
    """Returns the number of times each item in a list appears."""
    dict_with_counts: dict[str, int] = {}

    for item in input_list:
        if item in dict_with_counts:
            dict_with_counts[item] += 1
        else:
            dict_with_counts[item] = 1

    return dict_with_counts