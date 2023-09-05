# Sets

# A set is an unordered, unindexed collection, which does not allow for duplicates

# unindexed -> We cant use square brackets to access individual items
# unordered -> The ordering of the set may not represent the order the items were added


# A set can also be called a 'hashset', often seen in other languages. One really neat benefit
# a set gives, is that checking an item exists in the dictionary takes constant, and is fast!
# Sets don't allow for duplicates, which we can use to our benefit.
# Sets can only hold immutable items


# A set is constructed like this:
my_set = {1,2,3,4,5,6}
print("My set: ", my_set, "\n")
# We create an empty set like this
my_empty_set = set()

# We cant do:
# my_empty_set = {} # This is an empty dictionary!

# Sets do not allow for duplicates
set_with_repeaters = {1,1,1,2,2,2,3,3,3}
print(set_with_repeaters, "\n") # We're only left with {1,2,3}!

# This comes in useful for detecting and removing duplicates in lists/tuples/strings
# Heres a list of names, with a duplicate:
names = ["Sean", "Ian", "Adam", "Adam", "Jason"]
print("Duplicates are here:", names)

cleaned_names = set(names) # Passing the list into the set function takes care of duplicates!

print("Duplicates gone!", cleaned_names)
# Notice how the ordering is different? 


# lets take it a step further, and use the set function with some others.
# We have redefined names, as the sorted version of itself, with the duplicates taken out by the set function.
names = sorted(set(names))
print(names, "\n")


# If you just want to detect duplicates without removing them we can use the len() and set() functions together.
numbers = [10,20,30,30,40,50] # 30 appears twice

print("List length:", len(numbers)) # Length is 6
print("Set length:", len(set(numbers))) # the set() removes the additional 30, so the length is 5.

# Let's use an if statement to detect duplicates.
if len(numbers) == len(set(numbers)):
    print("There are no duplicates!")
else:
    print("There are duplicates!")
