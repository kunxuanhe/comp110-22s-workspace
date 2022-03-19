"""Some examples of tender, loving function definition."""


def love(name: str) -> str:
    """Given a name as a parameter, returs a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving measage n times."""
    love_note: str = ""
    i = 0
    while i < n:

        i += 1