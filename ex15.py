# Import the module argv from the sys library
from sys import argv

# Unpack the command line arguments into variables
script, filename = argv

# Open the file with the given name and assign it to a variable
txt = open(filename)

# Print a message with the filename
print(f"Here's your file {filename}:")
# Print the contents of the filename using the read() methid
print(txt.read())

# Close the first file object to free up resources and save changes
txt.close()

# Print a message asking for the filename again
print("Type the filename again:")
# Get the user input and assign it to a variable
file_again = input("> ")

# Open the file with the 'new' name and assign it to another variable
txt_again = open(file_again)

# Print the contents of the 'second' file by calling the read method on the file object
print(txt_again.read())

# Close the second file object to free up resources and save changes
txt_again.close()