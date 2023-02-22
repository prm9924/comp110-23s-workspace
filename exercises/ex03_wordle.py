"""Wordle structured with functions and six tries!"""

__author__ = "730573287"

def contains_char(word: str, character: str) -> bool:
    """This function checks if character exists in word"""
    assert len(character) == 1

    word_len: int = len(word)
    search_idx: int = 0
    char_in_word: bool = False
    while search_idx < word_len and not char_in_word:
        if character == word[search_idx]:
            char_in_word = True
        else:
            search_idx += 1
    return char_in_word


def emojified(guess: str, secret: str) -> str:
    """This function returns a string of colored boxes, checks to see if each letter in guess is in the right place when compared to secret"""
    assert len(guess) == len(secret)
    
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    secret_len: int = len(secret)
    searching_idx: int = 0
    emoji_result: str = ''

    while searching_idx < secret_len: # adds a green box if the letter is in the right spot
        if guess[searching_idx] == secret[searching_idx]:
            emoji_result += GREEN_BOX
        
        else: # adds yellow box if letter is in wrong spot, but exists in secret
            wrong_spot: bool = contains_char(secret, guess[searching_idx])

            if wrong_spot == True:
                emoji_result += YELLOW_BOX
            else:
                emoji_result += WHITE_BOX # adds white box if the letter was not found in any other index of secret
        
        searching_idx += 1
    
    return emoji_result


def input_guess(guess_length: int) -> str:
    """Tells the user to input a guess of the correct character length"""
    user_guess: str = input(f"Enter a {guess_length} character word: ")

    while len(user_guess) != guess_length:
        user_guess = input(f"That wasn't {guess_length} chars! Try again: ")
    
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = 'codes'
    playing: bool = True
    turn: int = 1
    
    while playing and turn <= 6:
        print(f"=== Turn {turn}/6 ===")

        guess = input_guess(5)
        attempt_result = emojified(guess, SECRET)
        print(attempt_result)

        if guess == SECRET:
            playing = False
            print(f"You won in {turn}/6 turns!")
        
        turn += 1
        
    if playing == True: # if playing never turns false but the while loop is exited, the user did not get the correct word within 6 tries
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()