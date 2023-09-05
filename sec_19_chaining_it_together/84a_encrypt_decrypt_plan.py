"""Encryption and Decryption program Plan."""
import os

os.system('clear')

### Read Text File Function ###
# This function accepts: the filename
# What does it do?
# it opens a file in read mode, and then returns the contents 
# as a lower case string.


### Encryption Function ###
# This function accepts: the plain text, and the shift.
# What does it do?
# This function iterates over the string.
# It then converts the string to its ASCII value, and applies a shift.
# This is then appended to the list, and then returned.


### Write Encrypted File Function ###
# This function accepts: the encrypted text, the filename
# What does it do?
# The function converts the list into a string.
# Then it adds 'ENCRYPTED_ to the filename.
# It then opens the file and writes the cypher text to it.


### Decryption Function ###
# This function accepts: the encrypted text, and the shift.
# What does it do?
# This function converts the string into a list.
# The list is iterated over, and with each character,
# we apply the reverse shift, and print it.


### Driver function ###
# This function accepts: The filename, shift, and the encryption mode.
# This function first opens the file ready for use.
# Then if in encrypt mode:
    # Pass the contents to the encrypt function
    # then pass them to the file write function
# then if in decrypt mode:
    # pass the contents to the decrypt function


