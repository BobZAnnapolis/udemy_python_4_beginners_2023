"""Higher/Lower Guessing Game."""
import random as ra
from datetime import datetime
import os

os.system('clear')


# This program allows the user to select a difficulty by first choosing the lowest
# and highest possible numbers the game will use. A random number is generated and then
# in a loop the user is prompted to make a guess, this guess is the compared to the actual
# number and a prompt is given depending on if they are correct, or higher/lower than the
# random number. During game play the number of guesses are counted and once the game is over
# then the game summary is written to a text file with the current date & time.


# ---Points for improvement---

# - Extend this program to ask the for the name in a safer way, perhaps with a while loop?

# - Write additional logic into the gameplay loop so that each guess is stored
#   in a list and then if the user makes a duplicate guess, they are warned?

# - Make the gameplay loop give a warning if a number is guessed that is outside
#   the range of what is allowed? (Say if the low, high is 1, 10 but the user guesses a 12 for example).

# - Write a function to read the existing score file to the user before gameplay commences.

# - Difficult.. Make this a 2 player game!


def establish_random_number(lowest: int, highest: int) -> int:
    """Return a random integer given the low and high points.
    
    Args:
        lowest: the lowest possible random number.
        highest: the highest possible random number.

    Returns:
        A random number between lowest and highest (inclusive of both).
    """
    pass


def create_save_file_text(name: str, guesses: int, lowest: int, highest: int) -> str:
    """Create the text to be appended to the save game file.
    
    Args:
        name: The name of the player.
        guesses: The number of guesses taken to guess the correct number.
        lowest: The lowest possible number, as defined by the player.
        highest: The highest possible number, as defined by the player.
    
    Returns:
        A string which details the game, to then be written to file.
    """
    pass


def write_text_to_file(filename: str, text: str, mode='a') -> None:
    """Write the text to file.
    
    Args:
        filename: The name of the file to be opened for appending.
        text: The text to be written to file.
        mode='a': Mode has been set to append, but can be changed if needed.
    """
    pass


def main_gameplay(random_number) -> int:
    """Gameplay loop.
    
    Args:
        random_number: this is the number the player is trying to guess.
        
    Returns:
        The number of attempts taken to guess correctly.
    """
    pass


def retrieve_lower_upper_numbers() -> tuple:
    """Retrieve the low/high numbers from the user.
    
    The user is prompted to enter the low/high numbers, and
    gets 3 attempts to do so. The try/except is to catch a situation
    where the integers are incorrectly entered. If the user exceeds the 
    number of attempt then they are given 1 & 10 by default.

    Returns:
        A tuple of the low and high numbers, used in random number generation.
    """
    pass


def main(filename: str) -> None:
    """Driver function to orchestrate gameplay.
    
    Args:
        filename: the name of the text file to be written to.
    """
    pass
