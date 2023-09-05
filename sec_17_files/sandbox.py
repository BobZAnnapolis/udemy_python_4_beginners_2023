import os

os.system('clear')

print("\nsection 17. FILES\n")

print("")
with open("/Users/bobzawislak/udemy/udemy_python/sec_17_files/75b_zen_of_python.txt", mode="r") as my_file:
    python_zen = my_file.read()
    print(f"len(python_zen): {len(python_zen)} characters\ttype(python_zen): {type(python_zen)}\tmy_file.read(): \n{python_zen}", "\n")
    print(python_zen)
    print("\n")
    word_count = len(python_zen.split())
    print(f"Number of words: {word_count}")

print(" ")

def hello_to_you(name: str) -> None:
    """Write a greeting to a text file."""
    # Write your code here
    file_name = "/Users/bobzawislak/udemy/udemy_python/sec_17_files/76a_greetings.txt"
    # if you run this, you will see a new file be created, with the contents of 'text_content' in that file.
    with open(file_name, mode="a") as my_file:
        my_file.write(f"Hello to you, {name}") # We can only pass strings here!
    
hello_to_you("Chris")
