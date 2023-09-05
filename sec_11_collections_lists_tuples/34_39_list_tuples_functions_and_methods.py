# Functions that work with Lists/Tuples and List/Tuple Methods

# Functions look like this:
# some_func(a)

# Functions are not bound to a type, for example the length (len) function
# works fine with strings, lists & tuples. 

# Functions don't just accept anything as the input though, for example if the length function
# was given an integer or a float, it would crash and raise a 'TypeError'.

# In this reference code I list all the most commonly used functions that can take a list/tuple as an input.


# NOTE: The functions below work the same with lists & tuples, unless indicate otherwise.


# -all-
# Returns True if everything in the list/tuple has a boolean value of True, otherwise False.
binary_nums = [1, 0, 1, 1, 0]
binary_nums_v2 = [1, 1, 1, 1]
print(all(binary_nums)) # False, because there are 0's in the list
print(all(binary_nums_v2), "\n\n") # True, because everything in the list has a boolean value of True!

# -any-
# Returns True if anything in the list/tuple has a boolean value of True, otherwise False.
strs_tuple = ("", "Yes", "No")
strs_tuple_v2 = ("", "", "")
print(any(strs_tuple))  # True, because 2 of the items have a boolean value of True
print(any(strs_tuple_v2), "\n") # False, because nothing is True


# -bool-
# Returns either True or False. The only list/tuple to return False is an empty one
print(bool([])) # False
print(bool([5,4,3]), "\n") # True

# -dir-
# Returns all the attributes a list/tuple has (All the things you can do with it!).
# print(dir(list), dir(tuple))
# Commented these out because they print a lot!


# -enumerate-
# This returns a collection of Tuples where each character of the sequence is paired
# with its index. We usually use this when iterating over strings (See Section 14 - Looping)
odd_nums = (1,3,5,7,9)
enumerated_tuple = list(enumerate(odd_nums))
print(enumerated_tuple, "\n")


# -help-
# Returns some quick scrollable documentation for the string.
# Useful if you dont fancy looking it up online!
# print(help(list)) # Commented out because it prints a lot!


# -isinstance-
# Returns True if the first argument 'is' a member of the second argument, False otherwise.
print(isinstance([6,5,4], list)) # True, because [6, 5, 4] is a list.
print(isinstance((3, 2, 1), list), "\n") # False, because (3, 2, 1),is a tuple.

# -len-
# Returns the length of the List/Tuple
names = ["Alex", "Chris", "Sue"]
print(len(names))
print(len((10,20,30,40,50)), "\n")


# -list-
# Converts its input to a list.
a_tuple = (99,88,77,66)
now_a_list = list(a_tuple)
print(now_a_list)

# Can also be combined with the range function!
one_to_ten = list(range(1,11))
print(one_to_ten, "\n")


# -map-
# Applies a function to each item in a sequence, and is often passed into a list/tuple.
# In this example, each country is passed to the len() function, then the results are stored in a list.
countries = ["Spain", "France", "Italy", "Sweden"]
length_countries = list(map(len, countries))
print(length_countries, "\n")


# -max-
# Returns the largest element (numerically or alphabetically)
print(max([1,2,3,4,5])) # Returns 5

trees = ("Willow", "Oak", "Pine")
print(max(trees), "\n") # Returns Willow

# -min-
# Returns the smallest element (numerically or alphabetically)
print(min([1,2,3,4,5])) # Returns 1

trees = ("Willow", "Oak", "Pine")
print(min(trees), "\n") # Returns Willow


# -reversed-
# Returns a reversed version of the list/tuple. In this example i've used list(), 
# but tuple() can also be used if required.
drinks = ["Coffee", "Tea", "Water", "Milk"]
reversed_drinks = list(reversed(drinks))
print(reversed_drinks, "\n")


# -sorted-
# Returns a sorted list of the input sequence. Ensure the elements of the list are either
# all numerical, or all strings (or any valid type), or a TypeError could be raised.
nums = (5,4,5,6,8,9,1,2,-1)
print(sorted(nums), "\n")

# Or you can sort in reverse
print(sorted(nums, reverse=True), "\n")


# -sum-
# Returns the sum of the input sequence.
totals_100 = [20,20,20,10,5,5,10,8,2]
print(sum(totals_100), "\n")


# -tuple-
# Converts its input to a tuple
this_is_a_list = ["Turing", "Lovelace", "Babbbage"]
this_is_a_tuple = tuple(this_is_a_list)
print(this_is_a_tuple, "\n")

# -type-
# Returns the type of its input. Very useful for checking!
print(type([1,1,1]), type((6,6,5)), "\n")


# -zip-
# Zips together n sequences (such as a list/tuple) and returns tuples of the zipped members.
# In this instance i've passed them to the list function to return a list of tuples.
# Note: if one input is longer than the other, then the 'zipping' stops at the end of the shortest one.
evens = [2,4,6,8,10]
odds = (1,3,5,7,9)
print(list(zip(odds, evens)), "\n")


#######################


# Methods look like this
# list_of_names.some_method()

# Suppose 'list_of_names' is a list, then 'some_method' is a function that belongs to the list type,
# there are only a handful of methods that exist across different types. For example, the 'count'
# method which counts the number of a given character within a variable exists for the string, list & tuple.

# Another easy way of telling apart a method and a function is that methods have dots between them and the variable.
# Some methods take additional inputs, whilst some do not. In this reference code I have included all list/tuple methods.

# I've roughly arranged these into sections, and added newline characters to break them up.


# Tuples only have 2 methods, 'count' & 'index', i've shown them here toegether with lists.

# -- Line 166: Adding to lists
# -- Line 208: Removing from lists
# -- Line 244: Rearranging lists
# -- Line 268: Showing information about lists/tuples


# -append-
# Adds a single item to the end of the list.
# This is an in-place operation, so it directly changes the list, without returning anything.
fib_numbers = [1,1,2,3,5,8]
print("Before appending: ", fib_numbers)
fib_numbers.append(13) # 13 is added to the end of the list.
print("After appending: ", fib_numbers, "\n")


# -extend-
# Add multiple items to the end of the list.
# .extend() takes an iterable such as a list, tuple or string, and adds each item in the iterable.
# This is an in-place operation, so it directly changes the list, without returning anything.
fib_numbers = [1,1,2,3,5,8]
print("Before extending: ", fib_numbers)
fib_numbers.extend([13,21,34]) # Adding 13,21,34 to the end of the list.
print("After extending: ", fib_numbers, "\n")

# -insert-
# Adds a single item at a chosen index in the list.
# This is an in-place operation, so it directly changes the list, without returning anything.
# Insert two two inputs. The index of where to insert the item, and the item itself.
fib_numbers = [1,1,2,3,8]
print("Before inserting: ", fib_numbers)
fib_numbers.insert(4, 5) # At index 4, insert the integer 5.
print("After inserting: ", fib_numbers, "\n")


# -copy-
# (whilst not strictly 'adding' to a list, i've added it here as it seems the most fitting!)
# This method returns a new list, with a copy of the elements from another.
names = ["James", "Alex", "Matthew", "Daniel", "Charlotte"]
names_again = names.copy()
print(names, names_again, "\n")
# 'names_again' is a shallow copy of 'names', meaning that you can change the original
# list without altering the copy.
# names_again = names --> doing this would be a deep copy, and changing 'names' would also change the other.
# Another way of doing a shallow copy is to do:
names_again_v2 = names[:]



# - remove-
# Removes a single item from the list
# This is an in-place operation, so it directly changes the list, without returning anything.
letters = ["A", "B", "C", "D"]
print("Letters before removal: ", letters)
letters.remove("A") # Removing A from the list
# letters.remove("X") # X is not in list, so a ValueError would be raised
print("Letters after removal: ", letters, "\n")

# -pop-
# Removes and returns the last element from the list. Or if a valid index is passed in
# then the item at this index is removed.
cities = ["Leeds", "London", "Liverpool"]
print("Cities before popping: ", cities)
popped_city = cities.pop() # 'popping' the last element
# popped_city = cities.pop(0) # 'popping' the first element
print("Popped city:", popped_city)
print("Cities after popping: ", cities, "\n")


# -clear-
# Removes every element from the list, leaving it as an empty list.
# This is an in-place operation, so it directly changes the list, without returning anything.
# Different to the del() function which deletes the variable identifier.
numbers = list(range(1,11))
print("Before clearing:", numbers)
numbers.clear() # Clearing out all the elements!
print("After clearing:", numbers)


# -reverse-
# Reverses the list
# This is an in-place operation, so it directly changes the list, without returning anything.
foods = ["Pasta", "Cheese", "Ham"]
print("Before reversal: ", foods)
foods.reverse()
print("After reversal: ", foods, "\n")


# -sort-
# Sort the list numerically or alphabetically, depending on the contents of the list
# You also have the option of sorting in reverse, and using a 'key' which is a
# function used to sort the function.
# This is an in-place operation, so it directly changes the list, without returning anything.

states = ["Maine", "New York", "Florida", "North Carolina"]
print("Before sorting: ", states)
states.sort() # Sorting normally (alphabetically).
# states.sort(reverse=True) # Sorting in reverse (alphabetically).
# states.sort(key=len) # Sorting by string length.
# states.sort(key=len, reverse=True) # Sorting by string length, in reverse.
print("After sorting: ", states)


# -count-
# This is for both Lists and Tuples!
# Returns the count of how many times an element appears in a list or tuple
# This method returns information, it doesn't change the list/tuple in any way.
odd_nums = (3,3,3,3,3,3,3,5,5,7)
print(f"3 appears {odd_nums.count(3)} times in the tuple.\n")


# -index-
# This is for both Lists and Tuples!
# This method returns information, it doesn't change the list/tuple in any way.
# This method raises a ValueError if the item is not in the list
mults_of_ten = list(range(10,110,10))
print("Multiples of 10", mults_of_ten)

item_to_search_for = 50
print(f"{item_to_search_for} is at index {mults_of_ten.index(item_to_search_for)}")
