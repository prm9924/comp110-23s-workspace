"""Fortnite, but based on chance!"""

__author__ = "730573287"

import random

points: int = 100
player: str = ""
playing: bool = True
still_standing: int = 100

HEALED_UP: str = "\U00002695"
MEDICAL_SYMBOL: str = "\U00002B06"
DAMAGED: str = "\U0001F915"
HEAVY_DAMAGE: str = "\U0001F4A5"


def greet() -> None:
    """Welcomes the player."""
    print("Welcome and thank you for playing Fortnite! In this battle royale, there are 100 players and you must survive to be the last one standing to \nearn a Victory Royale. You get 100 health points to start (max you can have is 200). Don't let it hit 0.")

    global player
    player = input("What is your name? ")


def roll_dice(points: int) -> int:
    """Custom fucntion which returns a roll of a dice. If users health points are low, they a more likely chance to die in the event of fight or more likely to gain health in the event of loot."""
    if points <= 200:
        result = random.randint(1, 6)
    if points < 100:
        result = random.randint(1, 5)
    if points < 50:
        result = random.randint(1, 4)
    
    return result
    

def experience() -> None:
    """Custom procedure in which the user chooses to fight, loot, or exit the game."""
    global points
    global playing
    global still_standing

    choice: int = int(input("Do you wish to fight another enemy player, find loot to get some useful items, or end the game? Click 1 to fight, 2 to loot, 3 to exit. "))
    
    assert choice == 1 or choice == 2 or choice == 3
    if choice == 3:
        print(f"It was fun while it lasted! You left the game with {points} health. Goodbye, stick around to perhaps be the last player standing next time!")
        playing = False

    if choice == 1:  # if user chose to fight, these are the possible outcomes of the fight.
        roll = roll_dice(points)
        if roll == 1:
            points -= 125
            print(f"{DAMAGED*2}{HEAVY_DAMAGE}")
            print("You took a lot of damage.")
        if roll == 2:
            points -= 75
            print(f"{DAMAGED*2}")
            print("You took significant damage.")
        if roll == 3:
            points -= 25
            print(f"{DAMAGED}")
            print("You took some damage.")
        if roll == 4:
            points += 100
            print(f"{HEALED_UP*3}{MEDICAL_SYMBOL*3}") 
            print("You won the fight and gained a lot of health.")
        if roll == 5:
            points += 75
            print(f"{HEALED_UP*2}{MEDICAL_SYMBOL*2}")
            print("You won the fight and gained significant health.")
        if roll == 6:
            points += 50
            print(f"{HEALED_UP}{MEDICAL_SYMBOL}")
            print("You won the fight and gained some health.")

    if choice == 2:  # if user chose to loot, these are the possible outcomes of opening a loot chest.
        roll = roll_dice(points)
        if roll == 1:
            points += 125
            print(f"{HEALED_UP*3}{MEDICAL_SYMBOL*3}")
            print("You found a chug jug in the chest. You gained a lot of health.")
        if roll == 2:
            points += 75
            print(f"{HEALED_UP*2}{MEDICAL_SYMBOL*2}")
            print("You found a slurp juice in the chest. You gained significant health.")
        if roll == 3:
            points += 50
            print(f"{HEALED_UP}{MEDICAL_SYMBOL}")
            print("You found some mini shields, you gained some health.")
        if roll == 4:
            points -= 25
            print(f"{DAMAGED}")
            print("The chest had poision in it, you lost some health.")
        if roll == 5:
            points += 0
            print("The chest was empty. You got nothing.")
        if roll == 6:
            points -= 100
            print(f"{DAMAGED}{HEAVY_DAMAGE*2}")
            print("The chest was planted with C4 by an enemy. You took a lot of damage.")

    if points <= 0:  # 0 points means no health points left, meaning user has died and lost the game.
        print("You died. Better luck next time.")
        playing = False
    if points > 200:
        points = 200
    
    num_eliminated = random.randint(1, 15)  # Randomly eliminates between 1 and 15 players each round since other players fight other players, not just the user.
    still_standing -= num_eliminated


def main() -> None:
    """Runs my version of Fortnite."""
    global points
    global playing
    global still_standing
    
    greet()
    
    while playing and still_standing > 1:
        print(f"You have {points} health and there are {still_standing} players left standing.\n")
        experience()
    
    if still_standing <= 1:
        print("Congratulations! You won a Victory Royale!")


if __name__ == "__main__":
    main()