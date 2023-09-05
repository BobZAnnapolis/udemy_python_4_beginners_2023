# Operators

# Operators are the symbols we tend to use in between values
# (We also call values 'operands')

# Consider the following:
# 10 * a
# 10 and 'a' are the operands
# * is the operator.

# This reference code will cover several types of operators, but we also look at operators throughout
# all the reference code so it isn't necessary to cover them in great detail here. For each
# type of operator we will also only cover the most commonly used ones.


# -Assignment Operators-
# Assignment operators work by giving a value to the operand on the left.

# Assigning 10 to the variable 'a'
a = 10
print("Original value of a:", a, '\n')

# A is now worth its original value, but increment by 10
a += 10
# Same as: a = a + 10
print("After incrementing by 10:", a, "\n")

# A is now worth its previous value, but decremented by 10
a -= 10
# Same as: a = a - 10
print("After decrementing by 10:", a, "\n")

# A is now worth its previous value, but mulitplied by 5
a *= 5
# Same as: a = a * 5
print("After multiplying by 5:", a, "\n")

# A is now worth its previous value, but divided by 2
a /= 25
# Same as: a = a / 25
print("After dividing by by 25:", a, "\n")


# -Comparison Operators-
# These work by comparing the two operands and giving either True or False.

value_a = 10
value_b = 25
print("Is equal:", value_a == value_b)
print("Is not equal:", value_a != value_b)
print("Is more than:", value_a > value_b)
print("Is less than:", value_a < value_b)
print("Is more than or equal to:", value_a >= value_b)
print("Is less than or equal to:", value_a <= value_b, "\n")


# -Membership Operators-
# These work by asking if the item in the left is in or no in the item on the right

# 'in' asks, 'is the item on the left in the item on the right?'
print(10 in [10, 2, -1]) # True, because 10 is in the list.
print(100 not in [10, 2, -1]) # True, because 100 is not in the list.
print(6 in {5,4,3}, "\n") # False, because 6 is not in the set.


# - Identity Operators-
# These work by checking that both operands are, or are not the 'same' object

# This can be a tricky one to figure out at first..
a = 100
b = a # Defining b to be a deep copy of a. They therefore 'point' to the same place in memory.
print(a is b) # True, because a and b refer to the same piece of data.
print(a is not b) # False.

# We can check by using the id() function to show the objects identity.
print(id(a), id(b), "\n") # These number are the same.

nums = [1,2,3]
shallow_copy = nums.copy() # The copy method returns a 'shallow copy'
print(nums is shallow_copy) # False, because it is a shallow copy.
