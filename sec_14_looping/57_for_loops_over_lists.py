# A for loop is a loop that is used to iterate over a sequence, or make a block of code repeat n times.
# In this reference file we mainly loop over lists, but there is an example using strings + tuples at the end.

# We arguably use for loops most commonly to iterate over sequences (such as a list, tuple or dict etc..)
# To 'iterate' means go over item by item.
# Suppose we have a list: nums = [10, 20, 30, 40]
# To iterate over nums would mean looking at each number in turn, and performing an action with each item.


numbers = [10, 20, 30, 40, 50]

for i in numbers: # For each item in numbers...
    print(i) # Do this!


# In the example above we used 'i'. This is just convention, and can whatever you like
# Uncomment the following to see an identical output to the code above.
# for number in numbers:
#     print(number)


# Whatever code is indented underneath the for statement is performed for each item in the list.
constant = 100
for i in numbers:
    print((i + constant) * 2)

# In this instance we define a variable as 100.
# Then for each number in the loop we print that number, with 100 added to it, then doubled.


# The indented block can do whatever you like, lets us an indented block along with an if/else statement.
# In this instance we iterate over the student scores and run each one through an if statement.

passed_students = 0
failed_students = 0
pass_mark = 55

student_scores = [65, 45, 21, 94, 86, 84, 82]

for score in student_scores:
    if score >= pass_mark:
        passed_students += 1
    else:
        failed_students += 1


print(f"{passed_students} students passed and {failed_students} students failed")



# In this example we iterate over a list of strings. If the string is a proper word (no numbers), then
# we print it in title case with a greeting.

potential_names = ["j0hn", "ian", "ch4rl011e", "chris"]

for name in potential_names:
    if name.isalpha():
        print(f"Hello, {name.title()}")


# In this example we iterate over a list and calculate the sum and product of the floats.

total = 0
product = 1

floats = [10.2, 4.2, -1.2, 6.6, 9.2]
for fl in floats:
    total += fl
    product *= fl


print("Total: ", total)
print("Product:", product, "\n")


# iterating over a string or a tuple looks just the same!
vowels = 'aeiou'
for vowel in vowels:
    print(f"{vowel.upper()} Is a vowel.")


tuple_of_cities = ("Leeds", "Manchester", "Liverpool")
for city in tuple_of_cities:
    print(f"{city} has {len(city)} letters.")