"""Encryption and Decryption program."""
import os

os.system('clear')

# This program can encrypt and decrypt text using a simple Casear Cypher.
# A caesar cipher simply 'shifts' a letter left or right, so a shift of +1 would take an 'a' to a 'b'.
# The reverse of this shift is then done to obtain the original value. This program runs in 2 modes:


# -Encryption Mode-
# A filename, and a shift is given (keep the shifts positive, and <= 15 for simplicity!)
# The program reads the text from the file, applies a shift to the ASCII value of each character
# then writes the cypher text to a new file. The cypher text uses the original file name but
# concatenates 'ENCRYPTED' before it.


# -Decryption Mode-
# A filename and a shift is given, the file is read and the reverse of the shift is applied to each
# value, then the ascii value is converted back to its alphanumerical form and printed to the screen.


# ASCII = American Standard Code For Information Interchange. This is a standardised encoding which
# maps each character to a number known as an 'ASCII Value'. The chr() function takes an integer and gives
# the corresponding alphanumeric value, and the ord() function takes a character and returns its ASCII value.


# What does if __name__ == "__main__" do?
# Here's the short answer, but this is worth reading up on!
# __main__ is a special variable that Python sets by itself, and when a script is directly ran,
# like when you open the file and hit 'Run' in Visual Studio Code, the value of __main__
# is set to '__main__'. If the script is imported into another program and indirectly ran, then it
# takes on the name of the filename (minus the .py). So the whole if statement is only ever true when
# run the file directly.


### How could you improve this??
## If the filename is invalid, could you use os.listdir() to print out text files in the current directory?
## Could you use a more advanced formula for encryption/decryption?

def read_text_file(filename: str) -> str:
    """Read text file and return contents.

     Args:
        filename: This is the name of the file to be read.

    Returns:
       A string of characters.
    
    """
    with open(filename, mode="r") as text_file:
        return text_file.read().lower()


def encrypt_text(plain_text: str, shift: int) -> list:
    """Encrypt plain text by applying a shift.
    
    This function takes the plaintext and a shift. each character
    is passed to the ord function to get its ASCII value, then a shift is
    added to that number.

    Args:
        plain_text: This is the plain text to be encrypted.
        shift: This is the shift to be added to the ASCII value for each character.
    
    Returns:
        A list of enrypted characters.
    """
    encrypted = []
    for char in plain_text:
        encrypted.append(str(ord(char) + shift))

    return encrypted


def write_encrypted_file(cypher_text: list, filename : str) -> None:
    """Write the cyphertext to a new text file.
    
    This function takes the cyphertext and original filename,
    then it joins 'ENCRYPTED' to the filename, and writes
    the cyphertext to this new file.

    Args:
        cypher_text: This is the encrypted string to be written to file.
        shift: This is the filename which is then used to make the new filename.
    """
    cypher_text_string = " ".join(cypher_text)
    cypher_file_name = "ENCRYPTED_" + filename
    with open(cypher_file_name, mode="w") as file:
        file.write(cypher_text_string)

    print("Cypher text saved to file:", cypher_file_name)


def decrypt_cyphertext(cypher_text: str, shift: int) -> None:
    """Decrypt cyphertext by applying the reverse of the shift.
    
    This function takes the encrypted string, and the shift.
    The string is iterated over, and the negative of the shift
    is applied to it to obtain the original character. The whole
    string is then printed.


    Args:
        cypher_text: This is the encrypted string, to be decrypted.
        shift: This is the shift, required to reveal the original character.
    """
    character_list = cypher_text.split()
    decrypted_text = ""
    for char in character_list:
        decrypted_text += chr(int(char) -shift)

    print("Decrypted text:\n", decrypted_text, sep="")


def driver_function(filename: str, shift: int, encrypt: bool = True) -> None:
    """Driver function to control subsequent encryption/decryption."""
    try:
        file_contents = read_text_file(filename)
    except FileNotFoundError as msg:
        print(f"'{filename}' does not exist, please try again.")
        return

    if encrypt:
        encrypted_text = encrypt_text(file_contents, shift)
        write_encrypted_file(encrypted_text, filename)
    else: 
        decrypt_cyphertext(file_contents, shift)


if __name__ == "__main__":
    # Use lines 73, 74 & 75 to encrypt a file by reading from 'secret_message.txt'
    # file = "secret_message.txt"
    # shift = 15
    # driver_function(file, shift, encrypt=True)

    # Use lines 78, 79 & 80 to decrypt, these are commented out and are just here for reference.
    file = "ENCRYPTED_hello.txt"
    #file = "zen_of_python.txt"
    shift = 15
    driver_function(file, shift, encrypt=False)
