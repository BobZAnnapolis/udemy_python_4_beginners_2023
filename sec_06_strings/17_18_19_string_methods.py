# Functions that work with strings & string methods


# Functions look like this:
# some_func(a)

# Functions are not bound to a type, for example the length (len) function
# works fine with strings, lists & tuples. 

# Functions don't just accept anything as the input though, for example if the length function
# was given an integer or a float, it would crash and raise a 'TypeError'.

# In this reference code I list all the most commonly used functions that can take a string as an input.


# -bool-
# Returns either True or False. The only string to return False is the empty string.
print(bool("")) # False
print(bool("Exists")) # True



# -dir-
# Returns all the attributes a string has (All the things you can do with it!).
# print(dir(str)) # You can pass 'str' directly.
my_string = "Coffee"
# print(dir(my_string)) # Or pass in a variable that holds a string.
# Commented these out because they print a lot!


# -enumerate-
# This returns a collection of Tuples where each character of the string is paired
# with its index. We usually use this when iterating over strings (See Section 14 - Looping)

# For this example we can pass the result to list to show a list of tuples.
# I show a better example of this in BLANK
print(list(enumerate("Food")))


# -help-
# Returns some quick scrollable documentation for the string.
# Useful if you dont fancy looking it up online!
# print(help(str)) # Commented out because it prints a lot!



# -id- 
# Returns the unique ID for a string (or any object), think of this roughly as relating to its memory address.
# If two different variables have the same ID, that means they are pointing to the same place in memory.
print(id("Memory"))
my_var = "Memory"
print(id(my_var) == id("Memory")) # This is True!


# -input-
# This prompts the user to input data, and returns it as a string.
# (I've commented these out so the code doesn't hang here!)
# a = input("Enter a name: ") # The user will see 'Enter a name: ', and their entered value is assignd to a
# b = input() # Also works without the prompt

# Note: if you're using input() to take in numbers, you'll need to pass it to int() or float().


# -int-
# Convers a valid string to an integer.
x = "10"
# x = "ten" # This would raise a ValueError.
x = int(x)
print(x, type(x))


# -isinstance-
# Returns True if the first argument 'is' a member of the second argument, False otherwise.
some_string = "This is most surely a string"
not_a_string = 3.14
print(isinstance(some_string, str)) # True
print(isinstance(not_a_string, str)) # False


# -list-
# Convert a string to a list.
letters = "ABCDE"
list_letters = list(letters)
print(letters, list_letters)


# -max-
# Return the maximum character from a string
# Max uses the ASCII value of a string to determine this --- See the ord() function.
print("Max:", max("abcd"))


# -min-
# Return the minimum character from a string
# Max uses the ASCII value of a string to determine this --- See the ord() function.
print("Min:", min("efgh"))


# -ord-
# Returns the ASCII value of a single character.
# ASCII = American Standard Code for Information Interchange.
print(ord('A')) # 'A' has an ASCII value of 65.


# -set-
# Convert a string to a set (Note that sets remove duplicates).
letters = "aabbccdeabca"
set_of_letters = set(letters)
print(letters, set_of_letters)


# -tuple-
# Convert a string to a tuple.
rock = "Sandstone"
tuple_rock = tuple(rock)
print(tuple_rock)


# -type-
# Returns the type of a variable, such as a string
print(type("Hello"))


# -zip-
# Zips together n sequences (such as a string) and returns tuples of the zipped members.
# In this instance i've passed them to the list function to return a list of tuples.
# Note: if one string is longer than the other, then the 'zipping' stops at the end of the shortest one.
str_one = "ACE"
str_two = "BDF"
print(list(zip(str_one, str_two)))


# Methods look like this
# name.some_method()

# Suppose 'name' is a string, we then 'some_method' is a function that belongs to the string
# type, there are only a handful of methods that exist across different types. For example, the 'count'
# method which counts the number of a given character within a variable exists for the string, list & tuple.

# Another easy way of telling apart a method and a function is that methods have dots between them and the variable.
# Some methods take additional inputs, whilst some do not. In this reference code I have included the most commonly used string methods.
# String methods do NOT change the string upon which they are called upon. they return a new string.

# I've roughly arranged these into sections, and added newline characters to break them up.

# -- Line 154: Checking strings (Returning True if the string is a certain way)
# -- Line 210: Converting string casings (Lower to upper case etc...)
# -- line 253: Checking the string for presence of characters
# -- line 296: Splitting and joining
# -- line 321: And the rest!



# -isalnum-
# Returns True if all characters are in the alphabet or are 0-9, False otherwise.
a_string = "abcde32"
another_string = "abc de32"
print(a_string.isalnum()) # True
print(another_string.isalnum(), '\n') # False, because of the whitespace.


# -isalpha-
# Returns True if all characters are in the alphabet, False otherwise.
a_string = "Christmas"
another_string = "Chr1stmas"
print(a_string.isalpha()) # True
print(another_string.isalpha(), '\n') # False, because of the '1'.


# -islower-
# Returns True if all characters are lower case, False otherwise.
a_string = "Christmas"
another_string = "Chr1stmas"
print(a_string.isalpha()) # True
print(another_string.isalpha(), '\n') # False, because of the '1'.


# -isupper-
# Returns True if all characters are upper case, False otherwise.
a_string = "ANGRY"
another_string = "anGRY"
print(a_string.isupper()) # True
print(another_string.isupper(), '\n') # False, because of the lower case 'an'.


# -isdigit-
# Returns True if all characters are digits, False otherwise.
a_string = "1234"
another_string = "1234!"
print(a_string.isdigit()) # True
print(another_string.isdigit(), '\n') # False, because of the '!'.


# -istitle-
# Returns True if string is in title case, False otherwise.
a_string = "Coffee"
another_string = "coffee"
print(a_string.istitle()) # True
print(another_string.istitle(), '\n') # False, because the string is lower case.


# -isspace-
# Returns True if all characters are, False otherwise.
a_string = "    "
another_string = "   -  "
print(a_string.isspace()) # True
print(another_string.isspace(), '\n') # False, because of the '-' in the middle.


#### Modifying the casings of strings #####


# -title-
# This converts the first letter of each word to upper case.
name = "ada lovelace"
titled_name = name.title()
print(name, titled_name)


# -lower-
# Converts all characters to lower case.
name = "aDa lOVElaCe"
lowered_name = name.lower()
print(name, lowered_name)


# -upper-
# Converts all characters to upper case.
name = "ada lovelace"
uppered_name = name.upper()
print(name, uppered_name)


# -capitalize-
# Converts only the first letter to upper case.
name = "ada lovelace"
capitalized_name = name.capitalize()
print(name, capitalized_name)


# -swapcase-
# Swaps the casings from upper/lower and vice versa.
name = "AdA LoVeLaCe"
swapped_name = name.swapcase()
print(name, swapped_name)


#### Checking the string for presence of characters #####


# -count-
# Returns how many times a character appears in a string.
my_string = "Python Programming"
print("Count of o characters: ", my_string.count("o"), "\n")


# -startswith-
# Returns True if the string starts with the given Prefix.
my_string = "Python Programming"
print("Starts with: ", my_string.startswith("Pyth")) # True
print("Does not start with: ", my_string.startswith("Lyth"), "\n") # False


# -endswith-
my_string = "Python Programming"
print("Ends with: ", my_string.endswith("ing")) # True
print("Does not end with: ", my_string.endswith("ing!"), "\n") # False


# -find-
# Returns the first index of where the character or substring is found.
# Will return a '-1' if not found.
my_string = "Python Programming"
print("First appears at: ", my_string.find("Prog"))
print("First appears at: ", my_string.find("X"), "\n")


# -index-
# Identical to find, but raises a ValueError if string is not found.
my_string = "Python Programming"
# print("Oops: ", my_string.index("X"), "\n")


# -rfind-
# Returns the LAST index of where the character or substring is found.
# Will return a '-1' if not found.
my_string = "Python Programming"
print("Last appears at: ", my_string.find("m"))
print("Last appears at: ", my_string.find("X"), "\n")


##### Splitting and Joining #####

# -split-
# Splits a string around a delimiter, and returns a list, by default the delimiter is whitespace.
sentence = "Python is pretty cool."

split_sentence = sentence.split() # No delimiter is passed in, so whitespace is used.
print("Split string: ", split_sentence)


names = 'John-Alex-Chris-Mark'
split_names = names.split('-') # This time we use '-' as the delimiter.
print("Split names: ", split_names)


# -join-
# Join takes some iterable such as a list or tuple, and joins the elements of that collection.
# together around a string, returning a string.
list_of_names = ["James", "Mark", "Ian"]

# In this example we are joining the names from the list with "---".
joined_names = "---".join(list_of_names)
print(joined_names, "\n")


##### And the rest! #####

# -strip-
# Removes whitespace from both ends of the string.
messy_string = "      hello     "
print(messy_string.strip())


# -lstrip-
# Removes whitespace from the left side of the string.
messy_string = "      hello     "
print(messy_string.lstrip())


# -rstrip-
# Removes whitespace from the right side of the string.
messy_string = "      hello     "
print(messy_string.rstrip())
# lstrip - from the left side 
# strip - all white space


# -replace-
# Replaces chosen characters from the string with others
# In this case we replace "0" with "e"
some_city = "Manch0st0r"
corrected_city = some_city.replace('0', 'e')
print("Corrected: ", corrected_city)
# replace(this, withThat, #) -> replace the # of this' withThats 