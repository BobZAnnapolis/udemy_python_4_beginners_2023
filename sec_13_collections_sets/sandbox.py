import os

os.system('clear')

print("\nsection 13. Sets\n")

print(" ")
lst = [10,10,10,20,30]
set_from_lst = set(lst)

print(f"lst = [10,10,10,20,20]\tprint(lst) : {lst}")
print(f"set_from_lst = set(lst)\tprint(set_from_lst : {set_from_lst})")

empty_set = set()
print(f"empty_set=set()\tprint(empty_set) : {empty_set}")
print("print(type(empty_set)) : ", type(empty_set))

print(" ")
