"""File to define Bear class!"""

__author__ = "730573287"


class Bear:   
    """Methods for a bear object."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Creates new bear in the river."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Bear age increases."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear gets less hungry the more fish it eats."""
        self.hunger_score += num_fish