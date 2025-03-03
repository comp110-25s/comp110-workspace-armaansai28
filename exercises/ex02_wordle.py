"""Wordle game coded"""

__author__ = "730560520"


def contains_char(search_length: str, character: str) -> bool:
    """Checks if the single character exists anywhere in the given string."""
    assert len(character) == 1, f"len('{character}') is not 1"

    index: int = 0
    while index < len(search_length):
        if search_length[index] == character:
            return True
        index += 1

    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Will return white, green, or yellow based on accuracy of users guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    result: str = ""
    index: int = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1

    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a word of expected_length"""
    guess: str = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """Where Wordle starts"""
    user_turn: int = 1
    total_turns: int = 6
    winner: bool = False

    while user_turn <= total_turns and not winner:
        print(f" === Turn {user_turn}/{total_turns} ===")
        guess: str = input_guess(len(secret))
        emoji_color: str = emojified(guess, secret)
        print(emoji_color)

        if guess == secret:
            winner = True
            print(f"You won in {user_turn}/{total_turns} turns!")
        else:
            user_turn += 1

        if not winner:
            print("X/6 - Sorry, try again tomorrow!~")


if __name__ == "__main__":
    main(secret="codes")
