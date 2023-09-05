# Functions that work with strings & string methods


# Functions look like this:
# some_func(a)

# Functions are not bound to a type, for example the length (len) function
# works fine with strings, lists & tuples. 

# Functions don't just accept anything as the input though, for example if the length function
# was given an integer or a float, it would crash and raise a 'TypeError'.

# In this reference code I list all the most commonly used functions that can take a dictionary as an input.
# I have also used the same dictionary throughout all functions, for ease of reading.

names_ages = {"John" : 25,
              "Alex" : 31,
              "Ada" : 22,
              "Sarah" : 30}


# -all-
# Returns True if all keys have a boolean value of True, otherwise False.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
print(all(names_ages))
print(all(names_ages.values()), "\n") # Pass the values instead.


# -any-
# Returns True if any keys have a boolean value of True, otherwise False.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
print(any(names_ages))
print(any(names_ages.values()), "\n") # Pass the values instead.


# # -dir-
# Returns all the attributes a dictionary has (All the things you can do with it!).
# print(dir(dict))
# Commented these out because they print a lot!


# -help-
# Returns some quick scrollable documentation for the dictionary.
# Useful if you dont fancy looking it up online!
# print(help(names_ages)) # Commented out because it prints a lot!


# -isinstance-
# Returns True if the first argument 'is' a member of the second argument, False otherwise.
print(isinstance(names_ages, dict)) # True
print(isinstance(names_ages, tuple), "\n") # False, because names_ages is not a tuple.


# -len-
# Returns the length of the dictionary, (by number of items.)
print(len(names_ages), "\n")


# -list-
# Returns a list of the dictionary keys or values.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
print(list(names_ages)) # List of the keys.
print(list(names_ages.values()), "\n") # List of the values.

# -map-
# Applies a function to each item in a sequence, and is often passed into a list/tuple.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
length_names = list(map(len, names_ages)) # Passing all names through the str() function.
string_ages = list(map(str, names_ages.values())) # Passing all ages through the str() function.
print(length_names)
print(string_ages, "\n")


# -max-
# Returns the maximum of either the keys or values.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
print(max(names_ages)) # Max of the keys.
print(max(names_ages.values()), "\n") # Max of the values.


# -min-
# Returns the mininum of either the keys or values.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
print(min(names_ages)) # Min of the keys.
print(min(names_ages.values()), "\n") # Min of the values.


# -set-
# Returns a set containing all the keys or values.
# NOTE: Dictionary keys have to be unique anyway, so using this function is probably limited in use.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
print(set(names_ages)) # A set of the keys
print(set(names_ages.values()), "\n") # A set of the values


# -sum-
# Calculates the sum of the keys or values.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
# print(sum(names_ages)) # Sum of the keys (Commented out as the keys in this dict. are strings!)
print(sum(names_ages.values())) # Sum of the values.


# -tuple-
# Returns a tuple of the dictionary keys or values.
# By default this will look at the keys, but you can use .values() to pass the dict. values to the function.
print(tuple(names_ages)) # Tuple of the keys.
print(tuple(names_ages.values())) # Tuple of the values.



# -type-
# Returns the type of its input. Very useful for checking!
print(type(names_ages), "\n")


#######################


# Methods look like this
# student_data.some_method()

# Suppose 'student_data' is a dictionary, then 'some_method' is a function that belongs to the dictionary type,

# Another easy way of telling apart a method and a function is that methods have dots between them and the variable.
# Some methods take additional inputs, whilst some do not. In this reference code I have included all dictionary methods.

# I've roughly arranged these into sections, and added newline characters to break them up.

# -- Line 137: Creating Dictionaries
# -- Line 153: Safely fetching, setting and updating data
# -- Line 185: Fetching keys values and items
# -- Line 207: Removing items from a dictionary


# -copy-
# Returns a dictionary which has a copy of all the items from another.
# This is a 'shallow' copy, which means that whatever happens to the original dict does not happen to the copy.
names_ages_copy = names_ages.copy()
names_ages["Sarah"] += 1
print(names_ages) # The original has been changed.
print(names_ages_copy, "\n\n") # The shallow copy is unaffected.


# -fromkeys-
# Created a dictionary by taking an iterable and turning these into keys, with a default value of 'None'.
# If a second argument is passed, then this is set as the value for each key.
blank = dict.fromkeys("ABCDE") # Makes a dict of 5 keys, each with a value of None.
blank_v2 = dict.fromkeys("FGHIK", 100) # Makes a dict of 5 keys, each with a value of 100.
print(blank)
print(blank_v2, "\n\n")


# -get-
# This method looks for a key and returns if it is present, or returns 'None' if not present.
# This is safe way of fetching data, as it avoids raising a possible KeyError, and saves a manual check.
# You may also pass a default return value as the second argument, which replaces 'None'.
stock = {"Banana" : 20, "Chicken" : 3, "Soup" : 8}
print(stock.get("Banana")) # Returns 20, as the key exists.
print(stock.get("Milk")) # Returns None, as the key does not exist.
print(stock.get("Milk", "Oops!")) # Returns "Oops!", as the key does not exist, and we provided a custom fallback message.


# -setdefault-
# This method allows for a key/value pair to be set, but only if the key is not already in the dictionary.
# This is a safe way of setting new data, as it prevents overwriting existing data.
# This is an in-place operation, which modifies the dictionary.
print("Before setting:", stock)
print(stock.setdefault("Banana", 44)) # This has no impact, as the key already exists.
print(stock.setdefault("Cheese", 100)) # This adds a key/value, as "Cheese" did not exist in the dict.
print("After setting:", stock, "\n")


# -update-
# This method updates one dictionary, with the contents of another.
# It will add new key/value pairs, as well as updating values.
# This is an in-place operation, which modifies the dictionary.
dict_one = {"A" : 100, "B": 200}
dict_two = {"B" : 250, "C": 300}
print("Before Updating", dict_one)
dict_one.update(dict_two)
print("After Updating", dict_one, "\n")


# -keys-
# Returns a dynamic view of the keys in the dictionary, which will show any changes that have occured.
# You can pass it to the list() function if you'd like to index, slice, or append etc...
print(names_ages.keys())
print(list(names_ages.keys()), "\n")


# -values-
# Returns a dynamic view of the values in the dictionary, which will show any changes that have occured.
# You can pass it to the list() function if you'd like to index, slice, or append etc...

print(names_ages.values())
print(list(names_ages.values()), "\n")


# -items-
# Returns a dynamic view of the items in the dictionary, which will show any changes that have occured.
# The items are given as a list of tuples.
# You can pass it to the list() function if you'd like to index, slice, or append etc...
print(names_ages.items())
print(list(names_ages.items()), "\n")


# -pop-
# Removes a chosen key/value pair from the dictionary, and returns the value.
# This is an in-place operation, which modifies the dictionary.
capitals = {"England" : "London",
            "France" : "Paris",
            "Greece" : "Athens"}

print("Before popping:", capitals)
removed_entry = capitals.pop("France")  # Removes item with a key of France, and returns the value.
print("Removed entry:", removed_entry) # Paris
print("After popping:", capitals, "\n")


# -popitem-
# Removes the most recently added key/value pair and returns it as a tuple -> (key,value)
# This is an in-place operation, which modifies the dictionary.
capitals = {"England" : "London",
            "France" : "Paris",
            "Greece" : "Athens"}

print("Before popping item:", capitals)
popped_item = capitals.popitem()
print("Popped item:", popped_item)
print("After popping item:", capitals)


# -clear-
# Removes all items from the dictionary.
# Different to the del() function which deletes the variable identifier.
capitals = {"England" : "London",
            "France" : "Paris",
            "Greece" : "Athens"}

print("Before popping item:", capitals)
popped_item = capitals.clear() # Dictionary is now clear.
print("After popping item:", capitals)

