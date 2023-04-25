"""File to define Fish class!"""

__author__ = "730573287"


class Fish:
    """Methods for a fish object."""
    age: int
    
    def __init__(self):
        """Creates a new fish in the river."""
        self.age = 0
        return None
    
    def one_day(self):
        """Fish age increases."""
        self.age += 1
        return None