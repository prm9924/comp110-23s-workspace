"""Asks user for a number, goes until they guess it right"""

SECRET: int = 4
guess: int = int(input("Guess a number: "))
playing: bool = True

while playing == True:
    if guess == SECRET:
        print('Yay! Correct')
        playing = False
    else:
        print('Wrong, guess again')
        if guess % 2 == 1: #guess is odd
            print('The answer is not an odd number')
        if guess > SECRET:
            print('Your guess is too high')
        else: #guess < secret
            print('Your guess is too low')
        guess = int(input('Next guess? '))