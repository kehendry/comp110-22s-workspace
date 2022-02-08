"""EX03 - Creating a Structured Wordle.""" 

__author__ = "730233362"


def contains_char(searched: str, searched_for: str) -> bool:
    """contains_char is true."""
    assert len(searched_for) == 1
    index = 0
    while index < len(searched):
        if searched_for == searched[index]:
            return True
        index = index + 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
alternate_index = 0 
index = 0
emoji_guess = str("")


def emojified(guess: str, secret: str) -> str:
    """Codifying responses."""
    index: int = 0
    emoji_guess: str = ""
    assert len(guess) == len(secret)
    while index < len(secret):
        if secret[index] == guess[index]: 
            emoji_guess = emoji_guess + GREEN_BOX 
        else:
            if contains_char(secret, guess[index]):
                emoji_guess = emoji_guess + YELLOW_BOX
            else:
                emoji_guess = emoji_guess + WHITE_BOX
        index = index + 1
    return emoji_guess


def input_guess(expected_length: int) -> str: 
    """Given an integer of expected length as a parameter."""
    guess: str = input(f"Enter a { expected_length } character word: ")
    while len(guess) != int(expected_length):
        guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    secret: str = "codes"
    has_won: bool = False
    while turns <= 6 and not has_won: 
        print(f"=== Turn { turns }/6 ===")
        guess: str = input(f"Enter a { len(secret) } character word: ")
        emojified(guess, secret)
        print(emojified(guess, secret))
        if guess == secret:
            has_won = True
            print(f"You won in { turns }/6 turns!")
        turns = turns + 1
    if turns >= 6: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()