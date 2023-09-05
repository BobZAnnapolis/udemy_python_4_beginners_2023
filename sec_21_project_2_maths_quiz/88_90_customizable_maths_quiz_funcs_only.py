"""Customisable Maths quiz."""
import random as ra
import os

os.system('clear')

# This program allows the user to test their mathematics skills by answering questions
# in addition, subtraction and multiplication. They are allowed to choose a difficulty
# and the number of questions. Then they choose from either a mixed bag of questions
# or purely addition, subtraction or multiplication.

# This is the largest program yet, and there is still ample room for improvements!

# ---Points for improvement---

# - Improve the choose_question_type() function by providing a limit on how many attempts they have to choose.
# - Extend this program by including division, modulus and exponentiation.
# - Improve the quiz by printing the correct answer when a mistake is made.
# - Extend the program by printing the results to a text file.


def choose_question_type() -> str:
    """Ask user for preferred type of maths question.
    
    The user is prompted to make a choice from the options available.
    The loop will continue to ask whilst their choice is not one of the
    available options from the list.

    Returns:
        The type of question to be used in the quiz.
    """
    pass

    
def choose_number_of_questions() -> int:
    """Ask user for number of questions they'd like to answer.
    
    Returns:
        the number of questions, which will determine loop size.
    """
    pass


def choose_difficulty_level() -> int:
    """Ask user for desired difficulty level.
    
    In the quiz we have 5 difficulty levels (1-5), where 1 is
    the easiest and 5 is the hardest. The difficulty level will
    be used later when generating questions. The higher the
    difficulty, the larger the numbers that are used.

    Returns:
        and integer from 1-5 representing difficulty level.
    """
    pass


def generate_numbers_for_question(difficulty_level: int) -> tuple:
    """Generate the numbers needed for the questions.

    Difficulty level 1: numbers 2 - 20
    Difficulty level 2: numbers 4 - 40
    Difficulty level 3: numbers 6 - 60
    Difficulty level 4: numbers 8 - 80
    Difficulty level 5: numbers 10 - 100
    
    Args:
        difficulty_level: A number from 1-5 relating to the difficulty of the question.
    
    Returns:
        A tuple of 2 numbers to be used in the question.
    """
    pass

def addition_question(operand_a: int, operand_b: int) -> bool:
    """Ask addition question, returning True if correct and False otherwise.
    
    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    pass

def subtraction_question(operand_a: int, operand_b: int) -> bool:
    """Ask subtraction question, returning True if correct and False otherwise.
        
    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    pass


def multiplication_question(operand_a: int, operand_b: int) -> bool:
    """Ask multiplication question, returning True if correct and False otherwise.
        
    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    pass


def main_game_loop(question_type: str, num_of_questions: int, difficulty_level: int) -> int:
    """Orchestrate the question loop and score keeping.

    This function consists of a for loop which loops for as many times as 'difficulty_level'
    For each cycle of the loop, the question type is examined which either picks a 'fixed' question
    or in the case when 'Mix' is selected a random question is chosen from the list. The score is kept
    during the quiz and incremented for each correct answer.
    
    Args:
        question_type: The type of questions to select (which function to call).
        num_of_question: Number of questions to answer (How long the loop runs for).
        difficulty_level: Determines the numbers to come from 'generate_numbers_for_question'.
        
    Returns:
        The number of correctly answered questions.
    """
    pass


def main() -> None:
    """Driver function to orchestrate maths quiz."""
    pass


if __name__ == "__main__":
    main()