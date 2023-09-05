import os

os.system('clear')

print("\nsection 14. Looping\n")

print(" ")

r = list(range(5))
e = list(enumerate(r))
print(f"range : {r}\nenumerate : {e}")

names_ages = {"Sue" : 45,
              "Rob" : 21,
              "Alex" : 31,
              "Ian" : 65}
for key, val in names_ages.items():
    print(f"key : {key}\tval : {val}")


nums = list(range(1, 10))
for num in nums:
    if num % 2 == 0:
        print(num * 5)


# This is the list you will be iterating over.
some_nums = [10, 54, 50, 99, -1, 12, 4, 66]
over_50 = []
### Write your code underneath this line ###
# Your task is to write a for loop which iterates over some_nums, adding the numbers that are above 50 to the blank list. For example if 'some_nums' contained [40, 87, 12, 99] then the 'over_50' list should have had 87 and 99 added to it to give [87, 99] at the end.
print(some_nums)
for num in some_nums:
    if num > 50:
        print(f"{num}") 
        over_50.append(num)
print(some_nums)
print(over_50)

# This is the dictionary to iterate over.
coffees = {"Brazil": 24,
           "Ethiopa" : 33,
           "Colombia" : 44,
           "Indonesia" : 10,
           "Honduras" : 8,
           "Vietnam" : 19}

# This is the stock level to check the coffees against.
minimum_stock_level = 20

# This is the list you will be populating.
order_required = []

# The goal of this exercise is to iterate over the keys & values in the dictionary and do the following:
# Look at each key/value pair
# If a coffee has less kilograms than the "minimum_stock_level'....
# Then add the key to the "order_required" list.
for country, count in coffees.items():
    print(f"{country} {count}")
    if count < minimum_stock_level:
        order_required.append(country)
print(f"We need coffee for the following : {order_required}")

print(" ")

### Random list generation code, do not touch this! ###
import random as ra
ra.seed(10)

grades = [ra.randint(1,100) for i in range(1000)]
total = 0
# You are given a random list of numbers called 'grades', and a variable set to 0 called 'total'. At the end of the exercise, the 'total' variable should contain the sum of the grades.
# There is also some pre-written code to generate this random list which you don't need to touch (we will be working with random numbers when we look at modules later in the course).
# Generally speaking, here's how this can be done.
# While the list still contains items..
# Remove an item and add that to 'total'
# How you construct the loop, remove the items and get the right total is up to you!
print(f"grades has {len(grades)} items")
print(f"BEFORE : sum of grades = {total}")
while len(grades) > 0:
    popped_val = grades.pop()
#    print(f"grades NOW has {len(grades)} items\tremoving {popped_val}")
    total += popped_val
print(f"AFTER : sum of grades = {total}")




print(" ")
