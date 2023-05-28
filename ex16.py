from sys import argv

script, filename = argv

txt = open(filename)

print(f"Hey there. This is what {filename} looks like: ")
print(txt.read())

print(f"We're going to erase {filename}.")
print("If you don't want that, hit 'control-C' (^C).")
print("If you do want that, hit 'return'.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

txt_again = open(filename)
print(f"This is what {filename} looks like now: ")
print(txt_again.read())
print("And finally, we close it.")
target.close()
