"""EX02 - One shot wordle - Guess in one go!"""

__author__ = "730573287"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
result: str = ""

SECRET: str = "python"
len_secret: int = len(SECRET)
guess: str = input(f"What is your {len_secret}-letter guess? ")

while len(guess) != len_secret: #tells user to use the correct word length
    guess = input(f"That was not {len_secret} letters! Try again: ")


while index < len_secret: #if a letter is in the right spot, the letter appears as a green box
    if guess[index] == SECRET[index]:
        result = result + GREEN_BOX

    else: #if a letter is in the wrong spot, checks to see if letter exists elsewhere in the word and prints a yellow box
        alt_index: int = 0
        wrong_spot: bool = False
        while wrong_spot == False and alt_index < len_secret:
            if guess[index] == SECRET[alt_index]:
                wrong_spot = True
            else:
                alt_index += 1
    
        if wrong_spot == True:
            result = result + YELLOW_BOX
        else: #white box appears if letter in not in the word
            result = result + WHITE_BOX

    index += 1 #goes through the while loop for all letters of the word

print(result)
if guess == SECRET:
    print('Woo! You got it!')
else:
    print('Not quite. Play again soon')