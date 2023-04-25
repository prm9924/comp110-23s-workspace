"""Challenge Question 04!"""

__author__ = "730573287"

def zip(strs: list[str], ints: list[int]) -> dict[str, int]:
    """Takes two lists and creates a dictionary with keys being items of the first list and values being items of the second list."""
    if len(strs) != len(ints):
        return {}
    
    new_dict: dict[str, int] = {}
    index = 0
    for item in strs:
        new_dict[item] = ints[index]
        index += 1
    
    return new_dict