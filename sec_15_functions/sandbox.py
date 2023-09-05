import os

os.system('clear')

print("\nsection 15. USER FUNCTIONS\n")

def add_one(num: int) -> int:
    """Returns the input val incremented"""
    return num +1

num = int(input("Enter a number : "))
ret_num = add_one(num)
print(f"add_one called with 7 : {add_one(7)}")
print(f"fcn add_one called with {num}, returns {ret_num}")
print("ADDONE Docstring: ", add_one.__doc__, "\n")
print("ADDONE type hints: ", add_one.__annotations__, "\n")



print(" ")



print(" ")
