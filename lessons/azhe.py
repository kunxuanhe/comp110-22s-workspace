"""How to draw boxes."""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret = "python"

guess = input("What is your len(secret) -letters guess? ")

while len(guess) != len(secret):
    guess = input("Try agian!")
i = 0
j = ""

while i < len(secret):
    if guess[i] == secret[i]:
        j = j + GREEN_BOX
    else:
        wording = False
        k = 0
        while k < len(secret) and not wording:
            if secret[k] == guess[i]:
                wording = True
            else:
                k += 1
        if wording:
            j = j + YELLOW_BOX
        else:
            j = j + WHITE_BOX
    i += 1

print(j)

if guess == secret:
    print("Yee.")
else:
    print("No.")