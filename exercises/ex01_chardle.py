"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730239053"

word: str = input("Enter a 5-character word: ")
character: str 

if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
else:
    character = input("Enter a single character: ")

if (len(character) != 1):
    print("Error: Character must be a single character. ")
    exit()
else:
    print("Searching for " + character + " in " + word)

i: int = 0

if (word[0] == character):
    print(character + " found at index 0")
    i = i + 1

if (word[1] == character):
    print(character + " found at index 1")
    i = i + 1

if (word[2] == character):
    print(character + " found at index 2")
    i = i + 1

if (word[3] == character):
    print(character + " found at index 3")
    i = i + 1

if (word[4] == character):
    print(character + " found at index 4")
    i = i + 1

if (i == 1):
    print(str(i) + " instance of " + character + " found in " + word)

if (i > 1):
    print(str(i) + " instances of " + character + " found in " + word)

if (i == 0):
    print("No instances of " + character + " found in " + word)