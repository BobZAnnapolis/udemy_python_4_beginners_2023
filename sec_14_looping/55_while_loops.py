# While Loops

# A while loop runs a block of code whilst a condition is True.
# A basic while loop has two parts, a condition and a code block.
# The condition is evaluated, and if True then the code block is ran.
# After the code block is executed the condition is evaluated again, and the process repeats.


# A basic while loop.
number = 1
while number < 10: # Whilst the number is less than 10, the indented code block runs.
    print("Loop condition satisfied. Number is:", number)
    number += 1 # After the print statement we increment the number by 1.


# Be careful to not produce an infinite loop!
# The example below (commented out) will run forever because the condition is always True!
#x = 5
#while x != 10:
#    print(x)



# In this example, we use a while loop to populate a list with additional 0's.
zeros = [0, 0]
desired_len = 6
while len(zeros) < desired_len: # While the length of the list is less than the desired length..
    zeros.append(0) # Add a zero to the end.
    print('0 appended to list.')


print("\n\n")
