# String Formatting

# In this reference code we will look at two types of string formatting.
# the .format() method, and "f-string"


# The format method takes a string with placeholders, and fills the placeholders with values

# This string contains two placeholders, the {} symbols.
some_string = "Hello my name is {} and I am {}."

# We then use .format() to populate these placeholders.
formatted_string = some_string.format("Alex", 21)

# "Alex" goes in the first placeholder
# 21 goes in the second placeholder

print("Formatted string: ", formatted_string, "\n\n")


#### f-strings ###

# f-strings do roughly the same job, but are arguably faster than the .format method()
# Rather than using the blank placeholders, we use the {} symbol, but pass the variable
# directly in. We always prefix an f-string with an "f".


city = "Liverpool"
duration = 4

sentence = f"f-strings : I live in {city} and have been there for {duration} years."
print(sentence)
