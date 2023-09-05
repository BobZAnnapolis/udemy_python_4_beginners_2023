import os

os.system('clear')

print("\nsection 6.17 Using Functions With Strings")

strVar = "Apple"
print("\nBOOL fcn\n\tif string has any chars init -> True")
print("strVar =",strVar,"\tprint bool(strVar)")
print(bool(strVar))
strVar = " "
print("strVar = ' '\tprint bool(strVar)")
print(bool(strVar))
strVar = ""
print("strVar = ''\tprint bool(strVar)")
print(bool(strVar))

strVar = "Apple"
print("\nDIR fcn\n\tlist the methods associated with the specified variable")
print("strVar = ", strVar,"\tprint dir(strVar)")
print(dir(strVar))

strVar = "Apple"
print("\nENUMERATE fcn\n\tPAIR each character with its index (have toconvert to a list toprint)")
print("strVar = ", strVar,"\tprint(list(enumerate(strVar)")
print(list(enumerate(strVar)))

# print("\nHELP(type) fcn\n\tlist all fcns associated with the type")
# print("help(str)")
# help(str)

print("\nID(var) fcn\n\tprints unique id of var, memory location")
print("print(id(strVar)")
print(id(strVar))

print("\nISINSTANCE(var,type) fcn\n\treturns bool -> is var of type type")
print("print(isinstance(strVar,str)")
print(isinstance(strVar,str))
intVar = 10
print("intVar=10\tprint(isinstance(intVar,int)")
print(isinstance(intVar,int))
print("print(isinstance(strVar,int)")
print(isinstance(strVar,int))

print("\nLIST(strVar) fcn\n\tconverts string into a list for list manipulation")
print(strVar,"\tprint(list(strVar)")
print(list(strVar))
print(" ")

print("\nORD(character): ordinal/ascii value of ()\nMIN(str): lowest ord val of str\nMAX(str): highest ord val of str\nCHR(val): character rep of (val)")
print("ord('A')\t", ord("A"))
print(strVar, "\tmax(strVar)", max(strVar))
print(strVar, "\tmin(strVar\t", min(strVar))
print("chr(71)\t", chr(71))
print(" ")

print("\nZIP(str1,str2)\n\tYields tuples until equal string size exhausted")
print("str1='Apple',str2='Kiwis',list(zip(str1,str2))")
str1 = "Apple"
str2 = "Kiwis"
print(list(zip(str1,str2)))
print("str2='Watermelon',list(zip(str1,str2))")
print(list(zip(str1,str2)))
print(" ")

print(" ")
