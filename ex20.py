from sys import argv

# unpack the command-line arguments into two variables
script, input_file = argv

# define a function that takes a file object as an argument and prints its content
def print_all(f):
    print(f.read())

# define a function that takes a file object as an argument and moves its pointer to the beginning of the file
def rewind(f):
    f.seek(0)

# define a function that takes a line number and a file object as arguments and prints the line number and the corresponding line from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open the input file in read mode and assign it to a variable
current_file = open(input_file)

print("First let's print the whole file:\n")

# call the print_all function to print the contents of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# call the rewind function to move the pointer to the beginning of the file
rewind(current_file)

print("Let's print three lines:")

# set the line number to 1
current_line = 1
# call the print_a_line function with the current line number and the current file as arguments
print_a_line(current_line, current_file)

# increment the current line number by 1 (=2)
current_line += 1
print_a_line(current_line, current_file)

# increment the current line number by 1 again (=3)
current_line += 1
print_a_line(current_line, current_file)
