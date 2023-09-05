# Iterating over Dictionaries


# When it comes to iterating over dictionaries, such as this one..

names_ages = {"Sue" : 45,
              "Rob" : 21,
              "Alex" : 31,
              "Ian" : 65}

# You can choose to iterate over the keys, values or items explicitly by using the
# dict.keys(), dict.values() or dict.items() methods respectively.

# By default, if we did 'for i in dict', we would iterate over the keys of that dictionary.


### Keys ###
for n in names_ages:
    print(n)

# Or we can use the .keys() method to get the same result.
for n in names_ages.keys():
    print(f"{n} is {names_ages[n]} years old.")

print("\n\n")



### Values ###
# To iterate over only the values of the dictionary we use dict.values().
# Lets do this to find the sum of ages.

total_ages = 0
for age in names_ages.values():
    total_ages += age

print("The sum of ages is:", total_ages, "\n")



### Items ###
# We use dict.items() to access each key/value individually.
for name, age in names_ages.items():
    print(f"Key: {name}, and the value... {age}")


# lets do another example to find the top scoring student.

students = "alex matthew mark sarah chelsea"
scores = [55,65,41,87,73]

# Create a dict. by zipping together the students and their scores.
student_scores = dict(zip(students.split(), scores)) 

max_student, max_score = "", 0 # Set some variables to be written to during the loop.


# As we iterate over the names and scores, we check them against the current max.
# If a students score is higher, then we replace the current max score and name with that student.
for student, score in student_scores.items():
    if score > max_score:
        max_student, max_score = student, score

print(f"The best student was {max_student.title()} with a score of {max_score}.")





