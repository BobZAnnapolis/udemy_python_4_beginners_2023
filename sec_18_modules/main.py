import os
from mymodule import add_two_nums as atn
import random as ra

os.system('clear')

print("\nsection 18. MODULES   \n")

# print(dir(mymodule))
#print(mymodule.name)
#print("THIS IN MAIN.PY", __name__)

#print(f"calling add_two_nums fcn in another module as atn(1,3) to add 2 nums : {atn(1,2)}")
#print(dir(ra))
print(f"print(ra.randint(1,5)) : {ra.randint(1,5)}")
print(f"print(ra.random()) : {ra.random()}")
print(f"print(ra.uniform(1,5)) : {ra.uniform(1,5)}")

names = ["Alex", "Bob", "Bob", "Bob", "Charles"]
print(f"\nnames -> {names}")
print(f"print(ra.choice(names)) : {ra.choice(names)}")

names = ["Alex", "Bob", "Charles", "Dave", "Ezra", "Franklin"]
print(f"\nnames -> {names}")
print(f"print(ra.choices(names, k=10)) : {ra.choices(names, k=5)}")
bias = [1, 1, 1, 1, 1, 1]
print(f"bias : {bias}")
print(f"print(ra.choices(names, weights=bias, k=5)) : {ra.choices(names, weights=bias, k=5)}")
bias = [1, 1, 1, 1, 1, 3]
print(f"bias : {bias}")
names = ["Alex", "Bob", "Charles", "Dave", "Ezra", "Franklin"]
print(f"print(ra.choices(names, weights=bias, k=5)) : {ra.choices(names, weights=bias, k=5)}")

names = ["Alex", "Bob", "Charles", "Dave", "Ezra"]
print(f"\nnames -> {names}")
print(f"print(ra.sample(names,k=2)) : {ra.sample(names, k=2)}")

cities = ["Alexandria", "Boston", "Charleston", "Detroit"]
print(f"\ncities -> {cities}")
ra.shuffle(cities)
print(f"print(ra.shuffle(cities)) : {cities}")

print(" ")

print("")
#from random import shuffle
nums = list(range(10))
print(f"nums = list(range(10)): {nums}")
ra.shuffle(nums)
print(f"shuffle(num): {nums}")