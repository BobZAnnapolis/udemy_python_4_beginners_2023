# We often use the range function to repeat a block of code a certain number of times, or to iterate 
# over the indices of a collection such as a list, string or tuple.

# As a recap, here's how the range function works. (I've combined it with the list functiion for easy reading)
# range(start, stop, step)

example_a = list(range(10)) # All integers from 0 up until 10. (10 is not included)
print("Example A", example_a)

example_b = list(range(2, 12)) # All integers from 2 up until 12. (12 is not included)
print("Example B", example_b)

example_c = list(range(10, 110, 10)) # All integers from 10 up until 110, in increments of 10. (110 is not included)
print("Example C", example_c, "\n")



# A basic usage is to use range() to make a block of code repeat n times.
for i in range(5):
    print("Hello!")

print("\n")


# We could also use the values produced by the range function.
for i in range(2, 8):
    print(f"It's a lovely day{'!' * i}")


print("\n")


# A common use case for range() is to access the indices of a sequence such as a list.
# We do this by passing the len() function to the range() function. So it iterates 
# in proportion to the size of the list.

names = ["Alex", "James", "Charlotte", "Matthew", "Daniel"]

# len(names) is 5.    -> So look at this as: range(5)
# range(5) produces 0,1,2,3,4.

for i in range(len(names)):
    print(f"Name: {names[i]} is at position: {i}")

print("\n")



# I'll include the enumerate() function here as this gives a similar result.
# The enumerate function returns each item as a tuple of the index and the item itself.
for index, name in enumerate(names):
    print(f"Name: {name} is at position: {index}")
