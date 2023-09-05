import os

os.system('clear')

print("\nsection 6.15 String Slicing")

print('\nstrVar = "Spaghetti"\tprint(strVar)')
strVar = "Spaghetti"
print(strVar)
print("0123456789")
print("Index positions")
print("Length")
length = len(strVar)
print(length)
print(" ")

print("print(strVar[3])")
print(strVar, strVar[3])
print("0123456789")
print(" ")

print("print(strVar[3:6])")
print(strVar, strVar[3:6])
print("0123456789")
print(" ")

print("print(strVar[4:7])")
print(strVar, strVar[4:7])
print("0123456789")
print(" ")

print("print(strVar[4:])\tfrom starting position to the end")
print(strVar, strVar[4:])
print("0123456789")
print(" ")

print("print(strvar[:5])\tfrom beginning to specified index")
print(strVar,strVar[:5])
print("0123456789")
print(" ")

print("STEP\nprint(strvar[0:length:2])\tskip over chars,specify start, end, # to jump")
print(strVar, strVar[0:length:2])
print("0123456789")
print(" ")

print("REVERSE\nprint(strvar[::-1])\t")
print(strVar, strVar[::-1])
print("0123456789")
print(" ")

print(" ")