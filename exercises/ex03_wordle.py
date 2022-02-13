"""EX03 - Structured Wordle."""

__author__ = "730463236"


def contains_char(guess_word: str, single_char: str) -> bool:
    """This looks for a specfic character within the string."""
    assert len(single_char) == 1
    i: int = 0
    check_var: bool = False
    while check_var is not True and i < len(guess_word):
        if single_char == guess_word[i]:
            check_var = True
            i = i + 1
        else:
            i = i + 1
    return check_var
            

def emojified(guess: str, secret: str) -> str:
    """This returns the emojis that signify the accuracy of the letters of the guess word in comparison to the secret word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_count: str = ""
    c: int = 0 
    while c < len(secret):
        if guess[c] != secret[c]:
            if contains_char(secret, guess[c]) is True:
                emoji_count = emoji_count + YELLOW_BOX
                c = c + 1
            else:
                emoji_count = emoji_count + WHITE_BOX
                c = c + 1 
        else:
            emoji_count = emoji_count + GREEN_BOX
            c = c + 1
    return emoji_count


def input_guess(exp_length: int) -> str:
    """The guess of the correct word length will be prompted for."""
    guess_word: str = input(f"Enter a {exp_length} character word: ")
    while len(guess_word) != exp_length:
        guess_word = input(f"That wasn't {exp_length} chars! Try again: ")
    return guess_word


def main() -> None:
    """This is the main loop for the Wordle game and start of the main program."""
    secret_word: str = "penispe"
    turn_count: int = 1
    the_guess: str = ""
    won_check: bool = False

    while turn_count <= 6 and won_check is False:
        print(f"=== Turn {turn_count}/6 ===")
        the_guess = input_guess(len(secret_word))
        print(emojified(the_guess, secret_word))
        if the_guess == secret_word:
            print(f"You won in {turn_count}/6 turns!")
            won_check = True
        turn_count = turn_count + 1
    if won_check is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
