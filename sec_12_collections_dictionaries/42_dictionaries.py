# Dictionaries, dict keys values & items.


# Dictionaries consist of key:value pairs
# Rather than using an index like in a string, list or tuple to access values we use keys.
# Dictionary keys MUST be immutable, for example a list may not be used as a key.

names_ages = {"John" : 30, "Alex" : 20, "Mike" : 44}
# This dictionary contains 3 items.
# The keys are, John, Alex, and Mike.
# The values are 30, 20 and 44.

# We access values like this:
print(names_ages["Mike"])

# This raises a KeyError, as the key does not exist in the dictionary.
# print(names_ages["Sue"])


# We can add new keys values like this:
names_ages["Alice"] = 33
print(names_ages, "\n") # We can see Alice added with a value of 33.


# We can change values like this:
names_ages["Mike"] = 45
print(names_ages) # Mikes age has gone from 44 to 45.


# There are 3 methods available which provide a dynamic 'view' into the dictionary.
# This means that they show the state of the data, with any changes thay may have been made.
# We will see these methods again when we iterate over dictionaries in section

# You can pass the result to the list() function to see it in a more presentable way
dict_keys = list(names_ages.keys()) 
dict_values = list(names_ages.values())
dict_items = list(names_ages.items())

print(dict_keys) # A list of the keys
print(dict_values) # A list of the values
print(dict_items) # A list of tuples (key: value)


# A really nice way to construct a dictionary is to combine the zip() and dict() function.
students = ["Sarah", "Ian", "Tim"]
scores = [55,54,61]

student_scores = dict(zip(students, scores))
print("Hey presto.. A dictionary! ", student_scores)


# A more presentable way of writing a dictionary is over multiple lines.
capitals = {"England" : "London",
            "France" : "Paris",
            "Greece" : "Athens"}


# Dictionaries can store pretty much anything...
details = {"Chris" : ["English", 55, "Accountant"],
           "Sarah" : ["French", 32, "Engineer"]}

# Accessing the list for Sarah, then going to index 2
print(details["Sarah"][2])


# You can store dictionaries.... in dictionaries
details_v2 = {"Sarah" : {"Job" : "Engineer", "Reports to" : "Lead Engineer"}}

# Accessing the value for Sarah, then accessing the 'Reports to' key from the inner dictionary.
print(details_v2["Sarah"]["Reports to"])