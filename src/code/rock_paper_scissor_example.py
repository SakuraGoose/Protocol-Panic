from random import randint
from enum import IntEnum


class Choice(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2

    def __str__(self):
        return self.name.capitalize()


def get_player_choice() -> Choice:
    """Anmod brugeren om at vælge mellem rock, paper og scissor."""
    while True:
        choice = input("Your choice (r - Rock, p - Paper, s - Scissor ): ")
        match choice.lower():
            case "r" | "rock":
                return Choice.ROCK
            case "p" | "paper":
                return Choice.PAPER
            case "s" | "scissor":
                return Choice.SCISSOR
            case _:
                print("Please enter r, p or s")


def display_result(player: Choice, computer: Choice):
    """Udregn vinder og vis resultatet.

    ### Parametre:
        - player (Choice): Spillerens valg.
        - computer (Choice): Computerens valg.
    """
    print(f"\nComputer choice: {computer}")
    print(f"Your choice: {player}")

    if player == (computer + 1) % 3 or (player == 0 and computer == 2):
        print("YOU WON!!!")
    elif player != computer:
        print("YOU LOST!!!")
    else:
        print("IT'S A TIE!")


def main():
    """Hovedfunktion."""

    player = get_player_choice()
    pc = Choice(randint(0, 2))
    display_result(player, pc)
    input("\nPress anything to exit...   ")


if __name__ == "__main__":
    main()
