"""Running the simulation of the river habitat!"""

__author__ = "730573287"

from exercises.ex09.river import River

my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()