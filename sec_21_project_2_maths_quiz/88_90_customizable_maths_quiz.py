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
    question_type = ["Addition", "Subtraction", "Multiplication", "Mix"]
    print(f"Choose from one of the following: {', '.join(question_type)}\n")
    choice = input("Enter choice here: ").title()

    while choice not in question_type:
        choice = input("Invalid choice, try again: ").title()
    else:
        return choice

    
def choose_number_of_questions() -> int:
    """Ask user for number of questions they'd like to answer.
    
    Returns:
        the number of questions, which will determine loop size.
    """
    try:
        num_of_questions = int(input("How many questions would you like? "))
    except ValueError:
        print("You entered an invalid input, defaulting to 10.")
        return 10
    else:
        if num_of_questions <= 0:
            print("Number of questions can not be negative, defaulting to 10.")
            return 10
        return num_of_questions


def choose_difficulty_level() -> int:
    """Ask user for desired difficulty level.
    
    In the quiz we have 5 difficulty levels (1-5), where 1 is
    the easiest and 5 is the hardest. The difficulty level will
    be used later when generating questions. The higher the
    difficulty, the larger the numbers that are used.

    Returns:
        and integer from 1-5 representing difficulty level.
    """
    while True:
        try:
            difficulty_level = int(input("Choose a difficulty level from 1-5: "))
        except ValueError:
            print("You entered the difficulty level incorrectly, try again.")
            continue
        else:
            if difficulty_level in range(1,6):
                return difficulty_level
            print("The number must be between 1 and 5.")
            continue


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
    operand_a = ra.randint(difficulty_level*2, (difficulty_level*20))
    operand_b = ra.randint(difficulty_level*2, difficulty_level*20)
    return operand_a, operand_b


def addition_question(operand_a: int, operand_b: int) -> bool:
    """Ask addition question, returning True if correct and False otherwise.
    
    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    try:
        question = int(input(f"What is {operand_a} plus {operand_b}? "))
    except ValueError:
        print("Answer entered in invalid format, moving to next.")
        return False
    else:
        return True if (question == operand_a + operand_b) else False


def subtraction_question(operand_a: int, operand_b: int) -> bool:
    """Ask subtraction question, returning True if correct and False otherwise.
        
    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    try:
        question = int(input(f"What is {operand_a} minus {operand_b}? "))
    except ValueError:
        print("Answer entered in invalid format, moving to next.")
        return False
    else:
        return True if (question == operand_a - operand_b) else False


def multiplication_question(operand_a: int, operand_b: int) -> bool:
    """Ask multiplication question, returning True if correct and False otherwise.
        
    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    try:
        question = int(input(f"What is {operand_a} multiplied by {operand_b}? "))
    except ValueError:
        print("Answer entered in invalid format, moving to next.")
        return False
    else:
        return True if (question == operand_a * operand_b) else False


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
    num_of_correct_answers = 0
    for i in range(1, num_of_questions+1):
        operand_a, operand_b = generate_numbers_for_question(difficulty_level)
        print(f"Question {i}")

        if question_type == "Addition":
            response = addition_question(operand_a, operand_b)
        elif question_type == "Subtraction":
            response = subtraction_question(operand_a, operand_b)    
        elif question_type == "Multiplication":
            response = multiplication_question(operand_a, operand_b)   
        elif question_type == "Mix":
            q_types = [addition_question, subtraction_question, multiplication_question]
            response = ra.choice(q_types)(operand_a, operand_b)
        
        if response:
            print("Correct!\n")
            num_of_correct_answers += 1
        else:
            print("Sorry, this is incorrect.\n")

    return num_of_correct_answers


def main() -> None:
    """Driver function to orchestrate maths quiz."""
    # First determine the type of questions to be answered.
    question_type = choose_question_type()
    if question_type == "Mix":
        print("You will receive a mix of questions.\n")
    else:
        print(f"You will only be tested on {question_type}\n")

    # Then determine how many questions are to be answered.
    num_of_questions = choose_number_of_questions()
    print(f"You will be answering {num_of_questions} questions.\n")

    # Then determine the level of difficulty.
    difficulty_level = choose_difficulty_level()
    print(f"You have opted for difficulty level: {difficulty_level}\n")

    # Then begin the main game loop
    correct_answers = main_game_loop(question_type, num_of_questions, difficulty_level)
    print(f"Quiz finished with {correct_answers} correct answers out of {num_of_questions}")


if __name__ == "__main__":
    main()