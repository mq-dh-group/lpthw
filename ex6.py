# Assign the number 10 to a variable named types_of_people
types_of_people = 10
# Create an f-string with the value of types_of_people and assign it to a variable named x
x = f"There are {types_of_people} types of people."

# Assign the string "binary" to a variable named binary
binary = "binary"
# Assign the string "don't" to a variable named do_not
do_not = "don't"
# Create an f-string with the values of binary and do_not and assign it to a variable named y
y = f"Those who know {binary} and those who {do_not}."

# Print the value of x
print(x)
# Print the value of y
print(y)

# Print an f-string with the value of x inside it
print(f"I said: {x}")
# Print an f-string with the value of y inside it
print(f"I also said: '{y}'")

# Assign the boolean value False to a variable named hilarious
hilarious = False
# Assign a string with a placeholder {} to a variable named joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the value of joke_evaluation with the value of hilarious inside the placeholder using the format () method
print(joke_evaluation.format(hilarious))

# Assign a string to a variable named w
w = "This is the left side of..."
# Assign another string to a variable named e
e = "a string with a right side."

# Print the concatenation of w and e using the + operator
print(w + e)