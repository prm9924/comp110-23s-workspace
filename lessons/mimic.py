def mimic(my_word: str, letter_idx: int) -> str:
    """prints the given character of the given word"""
    
    if letter_idx > len(my_word)-1:
        error_msg: str = 'Too high of an index'
        return error_msg
    else:
        your_character: str = my_word[letter_idx]
        return your_character


greeting: str = input('What is your word? ')
greeting_idx: int = int(input(f'Which index of \'{greeting}\' do you want to be displayed? '))
print(mimic(greeting, greeting_idx))