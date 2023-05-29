# import the argv module from the sys package
from sys import argv
# import the exists function from the os.path module
from os.path import exists

# unpack the command line arguments into variables
script, from_file, to_file = argv

# open the source file and read its data into a variable
in_file = open(from_file); indata = in_file.read()

# open the destination file in write mode and write the source file data to it
out_file = open(to_file, 'w'); out_file.write(indata)

# close both files
out_file.close(); in_file.close()
