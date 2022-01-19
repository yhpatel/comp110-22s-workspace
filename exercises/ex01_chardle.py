"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730463236"
print(__author__)

new_word: str = input("Enter a 5-character word: ")
if(len(new_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
one_chartr: str = input("Enter a single character: ")
if(len(one_chartr) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + one_chartr + " in " + new_word)
inst: int = 0

if one_chartr == new_word[0]:
    print(one_chartr + " found at index 0")
    inst = inst + 1
if one_chartr == new_word[1]:
    print(one_chartr + " found at index 1")
    inst = inst + 1
if one_chartr == new_word[2]:
    print(one_chartr + " found at index 2")
    inst = inst + 1
if one_chartr == new_word[3]:
    print(one_chartr + " found at index 3")
    inst = inst + 1
if one_chartr == new_word[4]: 
    print(one_chartr + " found at index 4")
    inst = inst + 1

if inst == 0:
    print("No instances of " + one_chartr + " found in " + new_word)
else:
    if inst == 1:
        print(str(inst) + " instance of " + one_chartr + " found in " + new_word)
    else: 
        print(str(inst) + " instances of " + one_chartr + " found in " + new_word)

