# While Loops

# A while loop runs a block of code whilst a condition is True.
# A basic while loop has two parts, a condition and a code block.
# The condition is evaluated, and if True then the code block is ran.
# After the code block is executed the condition is evaluated again, and the process repeats.

# There are 2 keywords that we can use to leave a while loop.
# These can be used in for loops, but are arguably seen more in while loops.


# -break- This leaves the loop completely.
# -continue- This stops the current iteration and goes back to the top to reelavuate the condition.



# In this basic example we use break inside an if statement
# If the number happens to be a multiple of 5, then we run a print statement then break out.
# Notice how the loop condition is to keep runniung whilst the number isless than 25,
# but the loop finishes early, when we hit 5.

number = 1
while number < 25:
    print("Number is currently:", number)
    if number % 5 == 0: # If the number is a multiple of 5...
        print("Breaking..") # Print this,
        break  # Then exit the loop completely!
    number += 1




# In this example we use a a while loop to ask the user to input a username.
# The loop will be an 'infite loop' because of the 'while True' part, but we use if statements
# inside the loop to break out when conditions are met.
# If we use more than 3 attempts we will break out the loop.
# If we enter an acceptable username we will also break out the loop.


attempts = 0 # Number of attempts starts at 0.
username = "" # Define a blank string.

while 0: # We can use True to create an infinite loop situation.
    if attempts == 3: # 
        print("All attempts used, a default has been given.")
        username = "John"
        break # We will break out of the loop if all attempts have been used.

    username = input("Enter a username longer than 5 characters: ")
    if len(username) > 5:
        print("Username entered successfully.")
        break # The loop can finish if the username is entered successfully.
    else:
        attempts += 1 # We will add 1 to attempts, if an invalid username is entered.


print("Loop finished, username is:", username, "\n")




# The continue statement behaves slightly differently than break.
# Rather than completely exiting the loop it will stop that current iteration,
# returning to the top and reevaluating the condition.
# I use a basic example here to demonstrate this.


number = 10
while number < 100:
    print("Number is:", number)
    if number == 50: # When the number becomes 50...
        print("Number is 50..")
        number += 5 # Increase it by 5,
        continue # Then stop the current cycle, returning to the top.


    number += 10 # When the number is 50, this line is never reached!

    


