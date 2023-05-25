# Assign a string with four placeholders to a variable
formatter = "{} {} {} {}"

# Print the variable with four integers as arguments
print(formatter.format(1, 2, 3, 4))
# Print the variable with four strings as arguments
print(formatter.format("one", "two", "three", "four"))
# Print the variable with four booleans as arguments
print(formatter.format(True, False, False, True))
# Print the variable with four copies of the same variable as arguments
print(formatter.format(formatter, formatter, formatter, formatter))
# Print the variable with four strings as arguments (it's the same as line 5 but using a new line for each argument)
print(formatter.format(
    "Late Night",
    "Lamont",
    "is my bias.",
    "This was written on four separate lines as four separate arguments but Python doesn't care."
))
