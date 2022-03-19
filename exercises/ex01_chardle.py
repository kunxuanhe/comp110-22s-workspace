"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730528983"

a_word: str = input("Enter a 5-character word: ")
if len(a_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit(0)

a_character: str = input("Enter a single character: ")
if len(a_character) != 1:
    print("Error: Character must be a single character.")
    exit(0)

print("Searching for " + str(a_character) + " in " + str(a_word))

if str(a_word)[0] == a_character[0]:
    print(a_character + " found at index 0 ")
if str(a_word)[1] == a_character[0]:
    print(a_character + " found at index 1")
if str(a_word)[2] == a_character[0]:
    print(a_character + " found at index 2")
if str(a_word)[3] == a_character[0]:
    print(a_character + " found at index 3")
if str(a_word)[4] == a_character[0]:
    print(a_character + " found at index 4")

number_of_characters = 0
if str(a_word)[0] == a_character[0]:
    number_of_characters += 1
if str(a_word)[1] == a_character[0]:
    number_of_characters += 1
if str(a_word)[2] == a_character[0]:
    number_of_characters += 1
if str(a_word)[3] == a_character[0]:
    number_of_characters += 1
if str(a_word)[4] == a_character[0]:
    number_of_characters += 1

if number_of_characters == 1:
    print("1 instance of " + a_character + " found in " + str(a_word))
if number_of_characters == 0:
    print("No instances of " + a_character + " found in " + str(a_word))
if number_of_characters == 2:
    print("2 instances of " + a_character + " found in " + str(a_word))
if number_of_characters == 3:
    print("3 instances of " + a_character + " found in " + str(a_word))
if number_of_characters == 4:
    print("4 instances of " + a_character + " found in " + str(a_word))
if number_of_characters == 5:
    print("5 instances of " + a_character + " found in " + str(a_word))
