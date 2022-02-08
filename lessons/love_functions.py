"""Some examples of tender, loving functions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = str("")
    counter: int = 0 
    while counter < n:
        # Concatenation
        love_note += love(to) + "\n"
        counter += counter
    return(love_note)