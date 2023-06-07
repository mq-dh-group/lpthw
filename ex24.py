print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
# note that this unpacks the typle returned in the function tuple to a new tuple
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# remember that using division / always results in a float numbers
start_point = start_point / 10

print("We can also do that this way")
# note that this variable holds the tuple as a whole
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string (unpacks the tuple)
print("We'd have {} beans, {} jars, and {} creates.".format(*formula))