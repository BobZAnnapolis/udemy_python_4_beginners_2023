# User defined functions part 3.

# In this demo code we look at making your functions look professional with:
# --annotations/type hints--
# --docstrings--

# Use the len function, and take note of what happens when you open the first rounded bracket.

# We see this...
# (__obj: Sized, /) -> int
# Return the number of items in a container.

# The top line are the function annotations, which tell us a bit more about the inputs and outputs.
# The second line is the docstring which gives us a description of what the function does.

# We can use annotations and docstrings to make code more professional, and give more insight
# to people using our code.

# Lets do a basic example, with a perimeter calculation function.
# In the first iteration there is no docstring or annotation.

def calculate_perimeter(height, length):
    return (2 * height) + (2 * length)


# Lets redefine it with a simple docstring in triple quotes.
def calculate_perimeter(height, length):
    """Returns the perimeter of a shape, given the height and length."""
    return (2 * height) + (2 * length)

# Now when we call it we can see the docstring in the pop up!
# or we can print it, using the .__doc__ attribute.
print("Docstring: ", calculate_perimeter.__doc__, "\n")





# In the second iteration lets add some basic annotations to give type hints.
# This tells the user that they should pass integers, and expect an integer back.
# Please note that Python does not actually check the types of these inputs, it merely 
# appears as a suggestion!
def calculate_perimeter(height: int, length: int) -> int:
    """Returns the perimeter of a shape, given the height and length."""
    return (2 * height) + (2 * length)



