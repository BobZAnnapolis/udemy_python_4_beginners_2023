# User Defined Functions

# A user defined function is a block of code we can create, and then re-use throughout our program.
# This saves us repeating ourselves and allows us to organise complex code into purpose built blocks.

# We have used plenty of built-in functions, such as max().
print(max([10,20,30]))

# The max() function takes an input and returns the maximum value of that input. It's useful because
# we can just use max(), rather than writing code for this manually every time. We should aim to create
# our own functions as much as possible to give us neat, clean and reusable code.

# Some key terms...

# def -> We use this to define a function.
# function name -> This is how we refer to our function.
# parameter(s) -> What the function takes as an input.
# argument(s) -> The actual value(s) we give to the function.
# return -> What the function gives back, and where the function stops and exits.

# A basic function to accept an input and 1 to it.

def add_one(value): # This takes one parameter (value)
    print(f"\tENTERing FCN add_one")
    return value + 1 # The functions stops here, giving back the input with 1 added to it.


# Lets call it!
my_value = 100
print(add_one(my_value), "\n") # Here we passed 'my_value' as the argument
# print(add_one()) # A TypeError is raised here as haven't passed an argument to the function.
# print(add_one('XYZ')) # This also raises an error as we can't add a string and an integer.


# Let's make the function more robust with an if statement.
def add_one_v2(value):
    print(f"\tENTERing FCN add_one_v2")
    if isinstance(value, (int, float)): # If the input is numerical, return the input + 1.
        return value + 1
    return 0 # If the if statement is not triggered, just return 0

print(add_one_v2("XYZ")) # This no longer causes the function to crash.
print(add_one_v2(999), "\n")


# Functions can take multiple values
def area(height, length): # Function takes 2 parameters (height and length.)
    print(f"\tENTERing FCN area")
    return height * length # Then if returns those multiplied together


print(area(100,5)) # We pass 100 and 5 as the arguments.
print(area(length=200, height=5), "\n") # We can also pass the arguments like this.



# Functions can take pretty much any type you like!
# In this case we define a function that returns a properly formatted name
# The if/elif/else considers the first argument and returns a formatted string.

def name_generator(gender, first, last): # There are 3 parameters
    print(f"ENTERing FCN name_generator")
    if gender == "male":
        return f"Mr {first.title()} {last.title()}"
    elif gender == "female":
        return f"Miss {first.title()} {last.title()}"
    else:
        return f"{first.title()} {last.title()}"


name_v1 = name_generator('male', 'john', 'smith')
print(name_v1)
name_v2 = name_generator('female', 'ada', 'lovelace')
print(name_v2)
name_v3 = name_generator('666', 'boo', 'yah')
print(name_v3, "\n")



#### Default Arguments ####
# A default argument is generally used when one of the inputs to the function
# stays the same, and is only sometimes changed. it allows us to 'fix' a value
# but gives us the option to change it when needed.

# in this case the sales_tax is predefined as 1.20, but we can pass it in and redefine it if we want to.

def tip_calculator(raw_cost, tip_amount, sales_tax=1.2):
    print(f"ENTERing FCN tip_calculator")
    cost_with_tip = raw_cost + tip_amount # First calculate raw cost with tip added.
    return round(cost_with_tip * sales_tax, 3) # Return total rounded to 3 decimal places.


meal = 95
tip = 16
final_cost = tip_calculator(meal, tip)
print("Final cost", final_cost)

final_cost_with_added_tax = tip_calculator(meal, tip, 1.35)
print("Final cost with more tax :( ", final_cost_with_added_tax)
