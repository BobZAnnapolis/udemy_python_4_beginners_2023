# Ints, Floats and Mathematics


# This reference code is broken down into different sections.

# -- Line 11: Converting between ints, floats & strings.
# -- Line 45: Adding, subtracting, Regular Division.
# -- Line 65: Exponentation, Floor Division and Modulus.
# -- Line 93: Order of Operations and PEMDAS


##### Converting between ints, floats & strings #####

# There are 3 functions which will be shown here:
# str() -> Converts its input to a string.
# int() -> Converts its input to an int.
# float() -> Converts its input to a float.

an_integer = 65 
a_float = 3.14

# Converting an int/float to a string is generally safe and wont raise an error.
str_int = str(an_integer)
str_float = str(a_float)
print(str_int, str_float, type(str_int), type(str_float), "\n")


# Converting to an integer is riskier, as the input has to be formed correctly.

# If converting a float, then it is rounded down if positive or rounded up if negative.
print(int(a_float))

# If converting a string, it has to be correctly formed.
print(int("6")) # This is fine.
# print(int("6!")) # This raises a ValueError.


# Converting an integer to a float.
print(float(an_integer))

# If converting a string, it has to be correctly formed.
print(float("2.4")) # This is fine.
# print(float("The 2.4")) # This raises a ValueError.


##### Adding, subtracting, Regular Division #####

# Any addition or subtraction involving a float will result in a float.
# Regular Division always gives a float.

# -Addition-
print(10 + 200)
print(an_integer + a_float)

# -Subtraction-
print(10 - 200)
print(an_integer - a_float)


# -Regular Division-
print(10 / 4)
print(an_integer / a_float)


##### Exponentation, Floor Division and Modulus #####

# -Exponentation-
# raises a base number (a) to some power (b).
# Written a ** b.
print(10 ** 3) # 10 to the power of 3.

# -Floor Division-
# This is just like regular division but the result is rounded down, and uses 2 slashes rather than 1.
print(10 // 4) # 10 divided by 4 is 2.5, but this rounds it down to 2.

# -Modulus-
# Modulus (or mod) is the remainder of floor division, and is done with the % operator.
# Take "10 mod 4" for example
# 4 fits in to 10 2 times, with 2 as the remainder. Therefore 10 mod 4 = 2

print(10 % 6) # 6 fits into 10 once, with a remainder of 4. So 10 % 6 == 4
print(100 % 30) # 20 fits into 100 3 times, with a remainder of 10. So 100 % 30 == 10
print(10 % 2) # 2 fits into 10 5 times, with a remainder of 0. So 10 % 2 == 0


# Modulus is the best way to figure out if a number is a multiple of x.
# We know 10 is even, so it should divide by 2 with no remainder
print(10 % 2 == 0) # Shows as True!
# Think of the line above as saying:
# "Does 10 divided by 2 have a remainder which is 0?"

print(11 % 2 == 0, "\n\n") # Shows as False, 11 is odd!


##### Order of Operations and PEMDAS #####
# Python follows the traditional order of operations (PEMDAS) and this states
# which order Python will look at an express or equation.

# PEMDAS = Parentheses, Exponents, Multiplication, Division, Subtraction.

a = 10
b = 5
c = 2

print((a + b) * c) # parentheses are done first, then the multiplication.
print((a + b) * c ** 5) # parentheses are done first, then the exponent, then the addition.

x = "two"
x = int(x)