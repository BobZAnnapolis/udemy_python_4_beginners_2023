
### Question 1.
### Given the following lists:
cameras = ["Canon", "Fujifilm", "Sony", "Nikon"]
new_cameras = []
# Iterate over 'cameras', and for each item append only the first and last letters
# of each string into the 'new_cameras' list, so the result looks like this:
# ["Cn", "Fm", "Sy", "Nn"]
# print(f"BEFORE : {new_cameras}")
# for c in cameras:
#     new_cameras.append(c[0] + c[-1])
# print(f"AFTER : {new_cameras}")

### Question 2.
# Given the following list:
numbers = [10,3,5,1,2,8,12]
# iterate over the list of numbers, and for each odd number:
# print its index, multiplied by the number.
# For example.. Index 1 contains number 3, so you would print 1 * 3.
# for idx, val in enumerate(numbers):
#     print(f"idx : {idx}\tval : {val}")
#     if ((not val % 2) == 0):
#         print(f"ODD  number {val} at idx {idx}\t {idx} * {val} = {idx * val}")
#     else:
#         print(f"EVEN number {val} at idx {idx}")


### Question 3:
# Given the following dictionary:
populations = {"townA" : 23000,
               "townB" : 15000,
               "townC" : 18000,
               "townD" : 35000}

# iterate over each dictionary item and for each entry..
# If the town has a population of 20000 or more print a string formatted like so:
# "townX has a large population of ...."
# If not, print a string formatted like so:
# "townX has a small population of ...."
for town, pop in populations.items():
    if pop >= 20000:
        print(f"{town} has a large population of {pop}")
    else:
        print(f"{town} has a small population of {pop}")