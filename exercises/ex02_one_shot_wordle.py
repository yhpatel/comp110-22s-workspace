"""EX02 - One Shot Wordle."""

__author__ = "730463236"

# This is where I defined the variables
secret_word: str = "python"
word_length: int = len(secret_word)
guess_word: str = input(f"What is your {word_length}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji_count: str = ""
i: int = 0
# This checks if the length of the guess word is equal to the word length
while len(guess_word) != word_length:
    guess_word = input(f"That was not {word_length} letters! Try again: ")
# This determines the color of the box for the assigned letter
while i < word_length:
    if guess_word[i] != secret_word[i]: 
        c: int = 0
        check_var: bool = False
        while check_var is not True and c < word_length:
            if guess_word[i] == secret_word[c]:
                check_var = True
                c = c + 1
            else:
                c = c + 1
        if check_var is True:
            emoji_count = emoji_count + YELLOW_BOX
        else:
            emoji_count = emoji_count + WHITE_BOX
    else:
        emoji_count = emoji_count + GREEN_BOX
    i = i + 1
# This is what prints the output
if guess_word == secret_word:
    print(f"{emoji_count} \nWoo! You got it!")
else:
    print(f"{emoji_count} \nNot quite. Play again soon!")