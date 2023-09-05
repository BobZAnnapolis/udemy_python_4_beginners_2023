import os

os.system('clear')

print("\nsection 11. Collections Lists & Tuples")

print("\n")

lst_names = ["James", "Alex", "Daniel"]
tup_names = ("James", "Alex", "Daniel")

#print("list: ", dir(lst_names))
print("\n")
#print("tuple: ", dir(tup_names))

a = list()
print("a = list() -> yields ", a)
b = tuple()
print("b = tuple() -> yields ", b)

print("list('ABCD') -> yields ", list("ABCD"))
print("tuple('ABCD') -> yields ", tuple("ABCD"))

# indexing 1 item in a sequence
# slicing is accessing N items

#             0         1            2         3          4
cities = ["London", "Liverpool", "Glasgow", "Leeds", "Sheffield"]
print("\n",cities)
print("     0          1           2          3          4")
print("\ncities[3] : ", cities[3])

print("\ncities[::-1]", cities[::-1])
print("\ncities[::2]", cities[::2])

print("\n")
names = ["James", "Ian", "Charlotte"]
print("names: ",names)
names.sort()
print("names.sort() :", names)
names.sort(key=len)
print("names.sort(key=len) :", names)
names.sort(key=len, reverse=True)
print("names.sort(key=len,reverse=True) :", names)


print(" ")
