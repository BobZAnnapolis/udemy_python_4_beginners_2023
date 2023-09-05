
### Question 1.
### Use a while loop to print the numbers from 35 to 65 (Including 65)
#print(list(range(35,66)))
# i = 35
# while i <= 65:
#     print(i)
#     i += 1
# else:
#     print("\tDONE !!")


### Question 2.
# Given the following list:
numbers = [10, 2, 8, 1, 12, 9]

### Use a while loop to repeatedly pop elements from the list, and
### add their total to a new variable called x.
### (So x should contain 10 + 2 + 8 + 1 + 12 + 9)
# x = 0
# print(numbers)
# print(f"BEFORE : {x}")
# while len(numbers) > 0:
#     num = numbers.pop()
#     print(f"Popped off : {num}\tadding to {x}")4

#     x += num
# print(f"AFTER : {x}")


### Question 3:
### Use a while loop, and the int() and input() functions to ask the user to enter a number.
### Whilst the number they entered is not a number between 1 and 10 (inclusive of 10),
### keep asking them.
### As a bonus, can you keep track of the number of attempts??
num = int(input("Please enter a number between 1 & 10 : "))
a = 1
while num <= 0 or num > 10:
    num = int(input(f"\n{num} is WRONG !! Try again (1 - 10: "))
    a += 1
else:
    print(f"\n\tCONGRATULATIONS !! You succeeded after {a} attempts. YOU KNOW HOW TO FOLLOW INSTRUCTIONS :-) \n")
