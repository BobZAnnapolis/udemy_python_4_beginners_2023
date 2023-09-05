# User defined functions part 2.

# In this demo code we will look at:
#  --chaining multiple functions together--
#  --returning more than 1 object from a function--

#  --chaining multiple functions together--

# Consider the following block of code:
num_as_string = "45.651" # First we define a string, that looks like a float.
rounded_num = round(float(num_as_string))
print("End Result: ", rounded_num, "\n")

# On line 11 we called 2 functions, round & float.
# When we call functions like this we always work from the inside out.
# So float(num_as_string) is called first...  Then the return value from that is given to round()
# Learning how to use functions like this is worthwhile as it results in cleaner and shorter code.

# In this example we will write two very simple functions and then chain them together.
# The first function will find the rough circumference, given the radius.
# The second function will take this value and return a nicely formatted string.
# A benefit of this is that this makes your code abide to the 'Single Responsibility Principle',
# where each function should only done one job!

def find_circumference(radius):
    return round((2 * 3.14159 * radius), 3)

def format_string(circumference):
    return f"The circumference is calculated to be: {circumference}"

# Then we chain the two calls together, and print the result!
result = format_string(find_circumference(130))
print(result, "\n")


#  --returning more than 1 object from a function--

# Functions can return more than one item, which can be really useful!
# First consider these few pieces of code...


first_last = ["Alan", "Turing"] # List contains two strings...
first, last = first_last # As the list contains two items, we can assign them to two variables!
print(f"First: {first}, Last: {last}\n")


evens = [2,4,6,8]
a, b, c, d = evens # In this case we assign 2,4,6,8 and to a,b,c,d respectively.
print(a, b, c, d, "\n")


odds = [1,3,5,7,9,11]
x, y, *z = odds #Using the asterisk here, we give the first and second items to x & y, then whatever is left to z.
print(x, y, z, "\n")


# The same principle applies to when we write a function that returns more than one item.

def return_multiples(num):
    return num*10, num*100, num*1000 # We are returning 3 values from this function.

# We could call is normally and the values would live in a tuple..
result = return_multiples(4)
print(result, type(result), "\n")


# Or we could unpack the result, like we did earlier!
first, second, third = return_multiples(65)
print(first, second, third)


# Or we could unpack the first item to the first variable and put the remaining values into a list.
first, *the_rest = return_multiples(77)
print(first, the_rest)

