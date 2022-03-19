"""An example of conditionals (if-else) statements."""

SECRET: int = 3


print("I'm thinking a number between 1-5, what is it?")
guess: int = int(input("what's your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have wonderfual day!!!")

else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You gussed too low!")
         


    print("Try running the program again.")

print("Game over.")



 