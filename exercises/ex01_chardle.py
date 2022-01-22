"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730528983"
a_word: str = input("Enter a 5-character word: ")
if len(a_word) == 5:
    print("You entered correct number of characters!!!")
else:
    print("Error: Word must contains 5 characters.")
    print("Try running the program again.")
    exit(0)

a_character: str = input("Enter a single character: ")
if len(a_character) == 1:
    print("Correct!")
else:
    print("Error: Character must be a single character.")
    print("Try running the program again.")
    exit(0)
    if len(a_character) >= 1:
        print("You entered more than one character.")
        exit(0)

print("Searching for " + str(a_character) + " in " + str(a_word))

if str(a_word)[0] == a_character[0]:
    print("Excellent! " + a_character + " found at index 0 ")
if str(a_word)[1] == a_character[0]:
    print("Excellent ! " + a_character + " found at index 1")
if str(a_word)[2] == a_character[0]:
    print("Excellent ! " + a_character + " found at index 2")
if str(a_word)[3] == a_character[0]:
    print("Excellent ! " + a_character + " found at index 3")
if str(a_word)[4] == a_character[0]:
    print("Excellent ! " + a_character + " found at index 4")

print("Searching for how many " + a_character + " in " + str(a_word))

count = 0
if str(a_word)[0] == a_character[0]:
    count += 1
if str(a_word)[1] == a_character[0]:
    count += 1
if str(a_word)[2] == a_character[0]:
    count += 1
if str(a_word)[3] == a_character[0]:
    count += 1
if str(a_word)[4] == a_character[0]:
    count += 1
print(str(count) + " instances of " + a_character + " found in " + str(a_word))