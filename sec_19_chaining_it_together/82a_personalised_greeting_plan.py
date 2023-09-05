"""Personalised Greeting Creator."""
# Import the random module
import os
import random as ra

os.system('clear')

### Set up some variables to be used in the program ###
# A list of template greetings
# A dictionary with numbers 1....n as keys, and the greetings as values.
greetings = ["Hey {}, I hope you are well!",
             "Whassup {}!",
             "Have a most splendid day {}"]
print(f"greetings=[. . .]:\n\t{greetings}")

dictionary_size = range(1, len(greetings)+1)
print(f"dictionary_size = range(1, len(greetings)+1):\n\t{dictionary_size}")

greetings_dict = dict(zip(dictionary_size, greetings))
print(f"greetings_dict= dict(zip(dictionary_size, greetings)):\n\t{greetings_dict}")

### Choose random template function ###
# This function accepts: Nothing.
# Uses the random module to select a random key from the greetings dict
# and then returning its value (a random template greeting)

### Choose greeting template function ###
# This function accepts: Nothing.
# Use user input to prompt the user to select a random greeting from the dict.
# This is then returned. We can choose a random one if they fail to choose correctly.

### Main 'run all' function ###
# This function accepts: Nothing.
# This first prompts the user for a name
# The it asks the user to choose between a fixed or random greeting.
# based on their choice we then call either the random or normal greeting
# function, and add their name to the template.

### Then set up variables and call functions.
# Step 1: Define the name of the text file.
# Step 2: Set up a variable to call the text file reader function and hold the string.
# Step 3: Then pass this variable to the parsing function and hold the results.
# Step 4: Then pass this variable to the frequency dict builder.
# Step 5: Iterate over the dictionary and print the words and their frequencies.
