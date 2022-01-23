"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730463236"

new_word: str = input("Enter a 5-character word: ")
if len(new_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
one_chartr: str = input("Enter a single character: ")
if len(one_chartr) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + one_chartr + " in " + new_word)
ct_inst: int = 0

if one_chartr == new_word[0]:
    print(one_chartr + " found at index 0")
    ct_inst = ct_inst + 1
if one_chartr == new_word[1]:
    print(one_chartr + " found at index 1")
    ct_inst = ct_inst + 1
if one_chartr == new_word[2]:
    print(one_chartr + " found at index 2")
    ct_inst = ct_inst + 1
if one_chartr == new_word[3]:
    print(one_chartr + " found at index 3")
    ct_inst = ct_inst + 1
if one_chartr == new_word[4]: 
    print(one_chartr + " found at index 4")
    ct_inst = ct_inst + 1

if ct_inst == 0:
    print("No instances of " + one_chartr + " found in " + new_word)
else:
    if ct_inst == 1:
        print(str(ct_inst) + " instance of " + one_chartr + " found in " + new_word)
    else: 
        print(str(ct_inst) + " instances of " + one_chartr + " found in " + new_word)