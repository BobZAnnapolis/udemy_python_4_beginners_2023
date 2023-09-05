import os

os.system('clear')

print("\nsection 12. Dictionaries")

print(" ")

names_ages = {"JOHN":20, "ALEX":31, "CHARLOTTE":19}
print(names_ages["JOHN"])

new_dict = dict()
new_set = set()
print("dict() :", new_dict, "\ttype(new_dict)", type(new_dict))
print("set() :", new_set, "\ttype(new_set)\n\n", type(new_set))

a = {"England": "London", "France": "Paris"}
print(a)
print("len(a): ", len(a))

people = ["Charlotte", "John", "Alice"]
scores = (85, 79, 80)

print("\npeople[] : ", people)
print("scores() : ", scores)

people_scores = dict(zip(people,scores))
print("people_scores = dict(zip(people,scores)) : ", people_scores)

print("people_scores['John'] :\n", people_scores["John"])

print("people_scores.keys() : ", people_scores.keys())
print("people_scores.values() : ", people_scores.values())
print("people_scores.items() : ", people_scores.items())

list_dict_keys = list(people_scores.keys())
list_dict_values = list(people_scores.values())
list_dict_items = list(people_scores.items())
print("list_dict_keys = list(people_scores.keys()) : ", list_dict_keys)
print("list_dict_keys[1] : ", list_dict_keys[1])
print("list_dict_values = list(people_scores.keys()) : ", list_dict_values)
print("list_dict_items = list(people_scores.keys()) : ", list_dict_items)

people_scores["BobZ"] = 13
print("\npeople_scores['BobZ'] = 13")
print("people_scores.keys() : ", people_scores.keys())
print("people_scores.values() : ", people_scores.values())
print("people_scores.items() : ", people_scores.items(), "\n")

capitals = {"England" : "London",
            "France" : "Paris",
            "Greece" : "Athens"}

print("Before popping:", capitals)
removed_entry = capitals.pop("France")  # Removes item with a key of France, and returns the value.
print("Removed entry:", removed_entry) # Paris
print("After popping:", capitals, "\n")

people = {
    "John": {"City": "London", "Age": 25},
    "Alice": {"City": "Leeds", "Age": 55},
}
print("BEFORE  John: ", people["John"])
print("BEFORE Alice: ", people["Alice"])
people["John"]["Sign"] = "Leo"
people["John"].setdefault("Food", "Cheese")
print("AFTER  John: ", people["John"])
print("AFTER Alice: ", people["Alice"])
print("people : ", people)

print(" ")