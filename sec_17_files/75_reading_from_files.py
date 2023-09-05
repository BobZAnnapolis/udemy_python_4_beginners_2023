# reading from text files

# In this reference code we will consider files that are in the same directory
# as your Python file, if the file is elsewhere you will need to provide the full path.

# When working with opening files, the default mode is 'r' for reading, so you can leave out the
# argument if you like. I like to explicitly pass the 'r' to make it obvious what i'm doing.
# We can also generally open files in 2 ways.

# Method 1: Explicitlly open, work on and then close the file.
# Method 2: use a 'with open' block which closes the file automatically at the end of the indented block.

# -Method 1-

# Open the text file in reading mode

# Here are 3 ways to get data from the file, it's important to note that you can't do all of these together,
# once the contents have been read, you'd need to reopen the file and read it again.

# Call the read method to return the file contents as one big string.
my_file = open("/Users/bobzawislak/udemy/udemy_python/sec_17_files/75a_mydetails.txt", mode="r")
file_contents = my_file.read()
print(f"len(fc): {len(file_contents)}\ttype(fc): {type(file_contents)}\tmy_file.read(): \n{file_contents}", "\n")
my_file.close()

# Call the readlines method to return a list of strings, where each string is a line from the file.
my_file = open("/Users/bobzawislak/udemy/udemy_python/sec_17_files/75a_mydetails.txt", mode="r")
file_lines = my_file.readlines()
print(f"len(fl): {len(file_lines)}\ttype(fl): {type(file_lines)}\tmy_file.readLines(): \n{file_lines}", "\n")
my_file.close()

# Call the readline method to return a single line from the file, subsequent calls return subsequent lines!
my_file = open("/Users/bobzawislak/udemy/udemy_python/sec_17_files/75a_mydetails.txt", mode="r")
single_line = my_file.readline()
print(f"len(sl): {len(single_line)}\ttype(al): {type(single_line)}\tmy_file.readLine(): \n{single_line}", "\n")
my_file.close()


# -Method2-
# Using this method is arguably simpler as the file is closed for us after the indented code has ran.
# Aside from this, we just use 'as xxxx' then we can call any of the aforementioned read methods on
# what ever name you have chosen.
# there's also no need to call .close()!
print("")
with open("/Users/bobzawislak/udemy/udemy_python/sec_17_files/75b_zen_of_python.txt", mode="r") as my_file:
    print('File contents...\n')
    print(my_file.read())


# Here's how you can handle situations where the file may not exist, using Try/Except
# to safely catch a FileNotFoundError.
print("")
filename = "/Users/bobzawislak/udemy/udemy_python/sec_17_files/something.txt"
try:
    with open(filename, mode="r") as some_file:
        print(some_file.read())
except FileNotFoundError:
    print(f"'{filename}' does not exist!")
