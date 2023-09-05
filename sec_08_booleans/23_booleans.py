# Booleans


# These are booleans, they can either be True or False
# We always write them like this, in title-case.
a_bool = True
another_bool = False

# Booleans are used in if statements, while loops and more!
# They are a pivotal part of control flow, and are worth fully understanding.

# Whilst we can define a variable as being True or False, we use booleans
# to decide whether conditions are True or False. For example, a log in system
# will need a password to be correct before allowing a user to log-in.
# The condition will be 'Is the password the same as the saved password?'
# This can either be True or False.

# lets start with some basic comparisons.

print(10 > 5) # We are printing "is 10 greater than 5?", yes it is, so this is the boolean True
print(6 == 3) # 6 and 3 are not the same, so we get False
print(10 > (2 + 2)) # 10 is greater than 4, so we get True


# Lets use the firs one in an if statement:
if 10 > 5:
    print("The condition is True, so I get printed!")

# The section after the 'if' is evaluated, if it is True, then the indented section will ran.


# Variables also have a 'boolean' value, and the bool() function can be used to check.
# generally speaking if something has a non-null, non-empty, or non zero value then it is True.
# To take strings, numbers, lists, dictionaries, tuples and sets as an example.

# Any empty string, lists, dictionary, tuple or set is False, otherwise True.
# Any float or integer that is 0 is False, otherwise True.

empty_list, empty_string = [], ""
print(bool(empty_list), bool(empty_string)) # Both False.

some_int, some_float = 100, 10.2
print(bool(some_int), bool(some_float)) # Both True.



###### and, or & not #####

# and, or & not are 3 boolean operators.

# -not-
# The job of 'not' is to flip a boolean from True to False, or False to True.
a = 10 > 2
print("A:", a) # A is true here, because 10 > 2.
a = not a
print("A:", a) # Not its false, because flipped it with 'not'.


# -and-
# and is an operator that looks at the values either side of it
# and gives a situation where it is only True it BOTH of those values are True.


condition_a = 10 > 2 # True
condition_b = 6 != 8 # True

# result is True because BOTH its operands are True.
result =  condition_a and  condition_b
print(result)

# In this situation we can also substitute the 'and' keyword for the ampersand operator.
result =  condition_a & condition_b
print(result)

# This one is False because the left operand is False.
print((10 == 11) and (2 > 0), "\n\n")


# -or-
# Or is similar to And, but it only requires one of the operands to be True

x = 10 == 12 # False
y = len("Hey") == 3 # True

# result is True because one of these operands is True (y).
result = x or y
print(result)

# In this situation we can also substitute the 'or' keyword for the vertical pipe operator.
result = x | y
print(result)


##### Some complex chaining! #####

#          True               # True
demo_a = (100 > 30) and (False or True)

# demo_a is True, because both side of the 'and' operator equate to True.
print(demo_a)

#        False           True           True
demo_b = False and ((6+1) == (7-0)) and "A" in "ABC"

# demo_b is False because the left most operand is False.
print(demo_b)