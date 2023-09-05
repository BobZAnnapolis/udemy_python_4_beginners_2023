import os

os.system('clear')

print("\nsection 6.14 String Indexing")

print('\ncity = "Manchester"\tprint(city)')
city = "Manchester"
print(city)
print("0123456789")
print("Index positions")
print(" ")

print("print(city[0])")
print(city[0])
print(" ")

print("print(city[0]) + !")
print(city[0] + "!")
print(" ")

print("1.PRINT LAST CHARACTER:Use length")
length = len(city)
print("length=len(city)\tprint(length)")
print(length)
print("print(city[length-1])\tchar positions start at 0")
print(city[length-1])
print(" ")

print("2.PRINT LAST CHARACTER:Use negative indexing")
print("print(city[-1])")
print(city[-1])
print(" ")

print("city[9] == city[-1]")
print(city[9] == city[-1])

print(" ")
