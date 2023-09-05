# Basic Control flow with 'if', 'elif' & 'else'


# -if statements-
# If statements comprise of a Condition and an indented block,
# the condition is evaluted, and if it evaluates to True then the indented block runs.

# In this example the condition is True, so the indented block runs.
value_a = 100
value_b = 200

if (value_a * 2) == value_b:
    print("Condition is True.")


# In this example, the condition is False, so the indented block did not run.
name = "Christopher"

if len(name) == 8:
    print("Name has a length of 8.")


# -if/else statements-
# the 'else' part of the statement gives your code the ablity to run a block
# of code, for situations where the condition was False. Let's use the previous example..


name = "Christopher"

if len(name) == 8:
    print("Name has a length of 8.")
else:
    print(f"Oops, {name} actually had a length of: {len(name)}")

# Because the if statement resulted in a False, the code jumped into the else
# section which ran instead.


# -if/elif/else statements-
# These statements allow for a secondary condition to be evaluated if the 'if' statement
# evaluates to False. You can stack elif statements together to make complex statements.

# Try changing the score to make different elif statements fire!
student_score = 55

if student_score >= 80:
    print(f"A score of {student_score} gets a grade A")
elif student_score >= 70 and student_score <= 79:
    print(f"A score of {student_score} gets a grade B")
elif student_score >= 60 and student_score <= 69:
    print(f"A score of {student_score} gets a grade C")
elif student_score >= 50 and student_score <= 59:
    print(f"A score of {student_score} gets a grade D")
else:
    print(f"A score of {student_score} is a failure.")

