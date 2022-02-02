"""EX02 - Creating a One Shot Wordle!"""

__author__ = "730233362"

secret_word: str = "python"

guess: str = input(f"What is your { len(secret_word) }-letter guess? ")

while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")
    print(guess)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


index = 0
emoji_guess = str("")
character_exists = False
alternate_index = 0 
while index < len(secret_word):
    if secret_word[index] == guess[index]: 
        emoji_guess = (str(f"{ GREEN_BOX }")) 
    else:
        character_exists = False
        alternate_index = 0
        while (character_exists is not True) and alternate_index < len(secret_word):
            if secret_word[alternate_index] == guess[index]:
                character_exists = True
            alternate_index = alternate_index + 1
        if character_exists:
            emoji_guess = str(f"{ YELLOW_BOX }") 
        else:
            emoji_guess = str(f"{ WHITE_BOX }")
    print(emoji_guess, end="")
    index = index + 1

print(end='\n')
if guess != secret_word: 
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")    
