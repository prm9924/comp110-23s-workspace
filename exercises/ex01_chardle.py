"""EX01 - Chardle - The first step towards wordle!"""

__author__ = "730573287"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + single_character + " in " + five_character_word)

num_matches: int = 0
if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    num_matches += 1
if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    num_matches += 1
if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    num_matches += 1      
if five_character_word[3] == single_character:
    print(single_character + " found at index 3") 
    num_matches += 1          
if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    num_matches += 1

if num_matches == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
elif num_matches == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)
else:
    print(str(num_matches) + " instances of " + single_character + " found in " + five_character_word)