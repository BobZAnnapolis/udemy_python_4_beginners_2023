# reading from text files

# In this reference code we will consider files that are in the same directory
# as your Python file, if the file is elsewhere you will need to provide the full path.

# We will be using 'with open' to open the files, see 'reading_from_files.py' for some example
# code on how this is is done.


# We will be looking at two modes in this reference code.
# w mode: Creates and then writes content to a new file (Caution! This can overwrite existing files!)
# a mode: Creates a file if not already in existence, or opens file if it exists. Content is then appended.


# -w mode-
# in this simple example we will write a simple string to a text file.
text_content = "This is some content I want to now be in a text file\n"
file_name = "/Users/bobzawislak/udemy/udemy_python/sec_17_files/76a_my_new_text_file.txt"


# if you run this, you will see a new file be created, with the contents of 'text_content' in that file.
with open(file_name, mode="w") as my_file:
    my_file.write(text_content) # We can only pass strings here!



# -a mode-
# In this example we will append some more content to the file we used above.
# This time we will use a for loop to write a couple of lines using data from a dictionary.

capitals = {"Monday" : "London",
            "Tuesday" : "Manchester",
            "Wednesday" : "Glasgow"}


with open(file_name, mode="a") as my_file:
    for key, value in capitals.items():
        write_string = f"On {key} I will travel to {value}\n" # Use the \n to write to a new line each time.
        my_file.write(write_string)

