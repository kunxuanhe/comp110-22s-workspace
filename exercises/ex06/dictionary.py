"""An example of three dictionary functions in Python."""

__author__ = "730528983"


# Function 1:
def invert(d: dict[str, str]) -> dict[str, str]:
    """Using invert as the first function and its key and value are strings."""
    # all_one is an empty dictionary.
    all_one: dict[str, str] = {}
    for key in d:
        if d[key] in all_one:
            raise KeyError("KeyError")
        all_one[d[key]] = key
    return all_one 


# Function 2:
def favorite_color(d: dict[str, str]) -> str:
    """This function describes favorite color using sting type."""
    # c is an empty dictionary.
    c: dict[str, int] = {}
    for key in d:
        if d[key] in c:
            c[d[key]] += 1
        else:
            c[d[key]] = 1
    max: str = ""
    for key in c:
        if max == "":
            max = key
        else:
            if c[key] > c[max]:
                max = key
    return max


# Function 3:
def count(ls: list[str]) -> dict[str, int]:
    """This function is to show the count of the number of times that value appeared in the input list."""
    # c is an empty dictionary.
    c: dict[str, int] = {}
    for key in ls:
        if key in c:
            c[key] += 1
        else:
            c[key] = 1
    return c


def main() -> None:
    """This is a main function to check the correctness of your favorite_color function."""
    print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))