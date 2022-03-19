"""An example of one shot wordle."""
__author__ = "730528983"

secret_word: str = "python"

a_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(a_word) != len(secret_word):
    a_word = input(f"That was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
q = ""
i = 0
while i < len(secret_word):
    if a_word[i] == secret_word[i]:
        q = q + GREEN_BOX
    else:
        n = 0
        boolean = False
        while n < len(secret_word) and not boolean:
            if secret_word[n] == a_word[i]:
                boolean = True
            else:
                n = n + 1
        if boolean:
            q = q + YELLOW_BOX
        else:
            q = q + WHITE_BOX
    i = i + 1

print(q)

if a_word != secret_word:
    print("Not quite. Play again soon! ")
else:
    print("Woo! You got it! ")