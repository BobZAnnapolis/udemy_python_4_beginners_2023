
### Question 1
### Write a function to accept a list and return a new list
### with the start and end elements removed. You may assume that the list 
### will have at least 5 elements when passed in.
### Example:
### If [1,2,3,4,5] is passed in, then [2,3,4] should be returned.
def ret_list(lst: str) -> str:
    return lst[1:-1]
#print(f"AFTER : orig {[1,2,3,4,5]}\tnew_list {ret_list([1,2,3,4,5])}")
print(f"AFTER : orig '0123456789'\tnew_list {ret_list('0123456789')}")
print("\n")

### Question 2
### Write a function to accept a string (st) and an integer (n).
### Return a new string where each string in the character is repeated
### n times.
### Example: if st = "Hello" and n=3,
### Then return: "HHHeeellllllooo"
def repeat_char(st: str, n: int) -> str:
    """accept string, integer - returns new string with each char repeated n times"""
    new_st = ""
    for x in st:
        print(f"next char is : {x}")
        new_st += x * n
    return new_st
print(repeat_char("Hello", 3))
print("\n")


### Question 3
### Write a function to accept a variable number of integers (Assume there will be at least 2.)
### Write code to make your function return a dictionary, with the following keys/values
### The keys will be integers that are passed in.
### The values will be the same as the keys, but raised to the power of 3.
### Example: if 2,5,3 are passed in,
### Then return: {2 : 8, 5 : 125, 3: 27}
def number_dict(*ints: int) -> dict:
    """take in variable num of args, return a dictionary with keys = original args * vals will be each arg raised to the power of 3"""
    new_dict = {}
    print(f"type(new_dict) : {type(new_dict)}")
    for i in ints:
        print(f"passed in val : {i}")
        new_dict[i] = i ** 3
    return new_dict
nd = number_dict(2,5,3)
print(f"returned dictionary looks like : {nd}\t with length {len(nd)}")

x = 4567
print(f"length of {x} is {len(str(x))}")

print(f"max(1,50,2) : {max(1,50,2)}")
print(" ")

def sum_of_digits(letters_nums: str) -> int:
    """Return sum of digits only."""
    # Write your code here
    ret_total = 0
    for d in letters_nums:
        print(d)
        if d.isnumeric():
            ret_total += int(d)
    return ret_total
print(f"sum_of_digits('A7ED4A9X2') : {sum_of_digits('A7ED4A9X2')}")