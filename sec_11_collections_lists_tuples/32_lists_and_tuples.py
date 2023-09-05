# Lists & Tuples

# In this reference guide we will build lists & tuples, and cover indexing & slicing.
# NOTE: Indexing & Slicing lists and tuples is identical to how we did it with strings!


# Lists and Tuples are similar in a number of ways but have their key differences.


# Lists & Tuples can both be sliced and indexed identically.
# Lists are mutable (they can be changed).
# Tuples are immutable (they can not be changed).
# Lists can be convereted to Tuples and vice versa.
# Lists are created with square brackets or the list() function.
# Tuples are created with rounded paretheses or the tuple() function. 


my_list = [1, 1, 2, 3, 5, 8]
my_other_list = list("ABCDE")

my_tuple = (13, 21, 34, 55)
my_other_tuple = tuple("FGHIJ")

print(my_list, my_other_list, "\n")
print(my_tuple, my_other_tuple, "\n")


# Mutability
# Let's try changing an element of a list & a tuple to see what happens.
lst = [1,2,3]
tup = (6,5,4)

print("Before:", lst, tup)

lst[0] = 100 # Setting the first index of lst to 100
# tup[0] = 200 # Uncomment this, what happens?

print("After:", lst, tup, "\n\n")
# We are able to change the list because is mutable,
# attempting this with the tuple gives a TypeError!


##### Indexing & Slicing ######

# This won't be in as much detail, as this has been covered
# in the string section. A list is used here, but this works identically
# with a tuple.

# index  0  1  2  3  4   5   6   7
evens = [2, 4, 6, 8, 10, 12, 14, 16]

# Indexing
a = 4
print(evens[0]) # Accessing index 0(2)
print(evens[2]) # Accessing index 2(6)
print(evens[a]) # Accessing index 4(10)
print(evens[a-1]) # Accessing index 3(8)

# Slicing
print(evens[2:4]) # Accessing indices 2 until 4(6,8)
print(evens[4:]) # Accessing all indices 4 onwards(10,12,14,16)
print(evens[:a]) # Accessing indices up until 4(2,4,6,8)
print(evens[1:6:2]) # Accessing indices 1 up until 6, but every other number(4,8,12)
rev_evens = evens[::-1] # Reversing the list


