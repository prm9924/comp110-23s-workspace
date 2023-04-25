"""File to define River class!"""

__author__ = "730573287"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Methods for a river object."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def check_ages(self):
        """Removes bears and fish that have age greater than 5."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

        surviving_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        return None

    def remove_fish(self, amount: int):
        """Removes amount number of fish from the river."""
        surviving_fish: list[Fish] = []
        for i in range(amount, len(self.fish)):
            surviving_fish.append(self.fish[i])
        self.fish = surviving_fish
        return None

    def bears_eating(self):
        """Removes fish and increases hunger score of bears when they eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Removes bears that are too hungry."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Models reproduction of fish in the river."""
        new_fish: int = (len(self.fish) // 2) * 4
        for i in range(new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Models reproduction of bears in the river."""
        new_bears: int = len(self.bears) // 2
        for i in range(new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Allows river to be printed in an easy to understand way."""
        print(f"~~~ Day {self.day}: ~~~\nFish Population: {len(self.fish)}\nBear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates 7 days of life in river."""
        for i in range(7):
            self.one_river_day()