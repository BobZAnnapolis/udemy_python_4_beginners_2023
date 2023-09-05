# Catching errors with Try and Except


# Given a tuple of 4 items, what happens if we try to access the 10th index?
some_nums = (4, 5, 6, 7)

# We would get an IndexError! (Hence why its commented out)
# tenth_elem = some_nums[10]

# In certain situations, especially when we allow for user input, open files or make web requests we
# have to deal with uncertainty. Using try/except blocks are a great way to deal with possible exceptions
# and tell Python to do something else, should an exception be raised.


# First, we'll deal with a blanket exception, given the example above.
# When this runs we instead see the print statement rather then the error.
# It's important to note that this a blanket execption, it won't catch specific errors
# We will do these further down in the demo code.


try:
    tenth_elem = some_nums[10] # First try and run this..
except Exception:
    print("An error occured!\n") # But if something goes wrong, do this instead!


# We can add an 'else' clause which only runs if no error is caught.
try:
    first_elem = some_nums[0] 
except Exception:
    print("An error occured!") 
else:
    print("No error occured, here's the first element:", first_elem, "\n")


# We can also add a 'finally' clause which runs regardless of an error being raised or not.
try:
    first_elem = some_nums[0] 
except Exception:
    print("An error occured!") 
else:
    print("No error occured, here's the first element:", first_elem, "\n")
finally:
    print("End of try/except\n")


# - Catching Specific Exceptions-
# I've only listed 6 common errors here, but there are a lot more you will encounter!

# IndexError - Accessing an index from a sequence that does not exist.
# KeyError - Accessing an invalid key from a dict, or removing an invalid item from a set.
# NameError - Referencing a variable that does not exist.
# ValueError - Passing a inappropriate argument to a function.
# TypeError - Performing an operation (such as addition) on operands that don't support it.


# -IndexError-
# We ask the user for an index to print, and use try/except to safely catch an invalid index.
some_nums = [10,20,30,40,50]
idx_to_print = int(input("Enter an index to access and print: "))

try:
    print(some_nums[idx_to_print])
except IndexError:
    print(f"{idx_to_print} is not a valid index\n")


# - KeyError-
capitals = {"England" : "London",
            "France" : "Paris",
            "Chile" : "Santiago"}

# We catch a KeyError because Italy does not exist in the dict.
try:
    print("The Capital of Italy is", capitals["Italy"])
except KeyError:
    print("Sorry, that key does not exist")
    print("The keys are:", ", ".join(capitals.keys()), "\n")


# -NameError-
# We catch a NameError because 'my_name' does not exist.
try:
    print(my_name)
except NameError:
    print('Sorry it looks like that variable does not exist!')


# -ValueError-
# We catch a ValueError, in case of an inapropriate argument being passed to the int() function.
try:
    day_of_month = int(input("Enter day of month in numerical form from 1 - 31: "))
except ValueError:
    print("Day of month was entered incorrectly!\n")


# -TypeError-
# We can catch a TypeError for when we try to use an operator on variables that don't support it.
# There are more cases when this error is raised, this is just one!

a = 100
b = "200"
try:
    print(a + b) # We can't add an integer and a string!
except TypeError:
    print("Addition is not supported between these two variable types\n")



# We can also cater for multiple errors occuring in the same block, by stacking the except blocks.
foods = ["Cheese", "Pasta", "Tomato", "Beef"]

try:
    index = int(input("Enter an index to print: "))
    print("Heres what you asked for! ", foods[index])
except ValueError: # We can catch a ValueError..
    print("You entered an input that could not be converted to an integer.\n")
except IndexError: # Or we can catch an IndexError!
    print("You entered an invalid index.\n")
except Exception: # Or in some rare cases, we can choose to catch anyting (Though this not ideal!)
    print("Something else seemingly went wrong....")


# We can also access the original error message, by using 'as' in our exceptions.
x,y = 100, "D"
try:
    print(x / y)
except TypeError as message:
    print("Type Error raised, here's the error:", message, "\n")