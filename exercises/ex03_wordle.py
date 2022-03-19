"""An example of function definition."""
__author__ = "730528983"
from xmlrpc.client import Boolean


secret = "codes"

WHITE: str = "\U00002B1C"
GREEN: str = "\U0001F7E9"
YELLOW: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> Boolean:
    """Contains_char is defined as a function and it can be determined as ture or false."""
    assert len(char) == 1
    z = 0
    while z < len(word):
        if char == word[z]:
            return True
        z += 1
    return False


def emojified(key: str, guess: str) -> str:
    """Emojified."""
    emoji = ""
    assert len(guess) == len(key)
    i = 0
    while i < len(key):
        if guess[i] == key[i]:
            emoji += GREEN
        else:
            if contains_char(guess, key[i]):
                emoji += YELLOW
            else:
                emoji += WHITE
        i += 1

    return emoji


def input_guess(num: int) -> str:
    """Input guess."""
    guess = input(f"Enter a {num} character word: ")
    while len(guess) != num:
        guess = str(input(f"That wasn't {num} chars! "))
    return guess


def main() -> None:
    """Main."""
    count = 1
    end = False
    while not end and count < 7:
        print(f"=== Turn {count}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {count}/6 turns!")
            end = True
        else:
            count += 1
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()