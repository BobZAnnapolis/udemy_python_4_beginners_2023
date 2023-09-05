"""Word Frequency Counter."""
import os

os.system('clear')

### Read Text File Function ###
# This function accepts: the filename
# What does it do?
# This function opens a text file in read mode,
# and then returns the contents of the file as a string.


### File Contents Parser Function ###
# This function accepts: the raw text from the file
# What does it do?
# This function iterates over the raw text and for each character:
# if the character is alphanumeric, or a space character we add it to 
# a variable local to the function. This is then split and returned 
# as a list.


### Frequency Dictionary Builder Function ###
# This function accepts: the list of parsed words.
# What does it do?
# This function creates a blank dictionary, and then iterates
# over the list of parsed words. For each word in the list:
# if not in the dictionary, add it with a value of 1.
# If in the dictionary, increase its value by 1.
# Sort the dictionary according to their values, and return it.


### Then set up variables and call functions.
# Step 1: Define the name of the text file.
# Step 2: Set up a variable to call the text file reader function and hold the string.
# Step 3: Then pass this variable to the parsing function and hold the results.
# Step 4: Then pass this variable to the frequency dict builder.
# Step 5: Iterate over the dictionary and print the words and their frequencies.






