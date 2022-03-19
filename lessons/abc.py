"""Question 23."""


def odd_and_even(a: list[int]) -> list[int]:
    """lalalala."""
    new: list[int] = []
    for x in a:
        if x % 2 != 0:
            new.append(x)
    return new
