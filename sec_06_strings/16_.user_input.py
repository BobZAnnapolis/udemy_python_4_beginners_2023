import os

os.system('clear')

print("\nsection 6.16 Catching User Input")

# define an identifier. . . Program waits. . USER decides the value
# built-in function -> input()
name = input("\nEnter a name please : \n-> ")
print("User entered : ",name, "of type : ", type(name))
print(" ")

strVar = "California"
print(strVar)
print("0123456789")
idx = int(input("Enter a character index (integer) : "))
print("User entered : ",idx)
print(strVar[idx])

print(" ")
