"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730233362"

from operator import index


special_word: str = input("Enter a 5-character word: ")


if len(special_word) != 5:
    exit("Error: Word must contain 5 characters")

character: str = input("Enter a single character: ")

if len(character) > 1: 
    exit("Error: Character must be a single character.")

print("Searching for " + character + " in " + special_word)


if special_word[0] == character: 
    print(character + " found at index 0")

if special_word[1] == character: 
    print(character + " found at index 1")

if special_word[2] == character:
    print(character + " found at index 2")

if special_word[3] == character:
    print(character + " found at index 3")

if special_word[4] == character: 
    print(character + " found at index 4")


if special_word.count(character) == 1: 
    print("1 instance of " + character + " found in " + special_word)
else: 
    if special_word.count(character) == 2: 
        print("2 instances of " + character + " found in " + special_word)
    else:
        if special_word.count(character) == 3:
            print("3 instances of " + character + " found in " + special_word)
        else:
            if special_word.count(character) == 4:
                print("4 instances of " + character + " found in " + special_word)
            else: 
                if special_word.count(character) == 5:
                    print("5 instances of " + character + " found in " + special_word)
                else: 
                    print("No instances of " + character + " found in " + special_word)
