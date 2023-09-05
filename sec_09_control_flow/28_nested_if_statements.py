# Nested if statements

# 'nested' in Python generally means to put code inside other code of the same type.
# We can have nested for loops, nested while loops, and nested if statements.. to name a few!


# A good example of this is a quick sign-up program that asks for 
# a username and an age, with some constraints.
# The username must have at least 5 letters, and contain only letters,
# The age must be at least 18.



print("A username must be at least 5 characters and contain only letters.")
username = input("Please enter a username: ")

if len(username) >= 5 and username.isalpha():
    print("Username accepted, now please enter your age. This must be over 18.")
    age = int(input("Enter age: "))
    if age >= 18:
        print("Age accepted.")
    else:
        print("Age not accepted.")
else:
    print("Username not accepted.")


# In this example, if the first 'if' statement evaluates to True, only then
# do we proceed to ask for, and evaluate the age. If the first 'if' satement fails
# then we jump to line 24, and don't bother asking for the age.

