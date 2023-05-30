# Define a function called cheese_and_crackers that takes two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# Call the function with 20 and 30 as arguments
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# Define two variables with values 10 and 50
amount_of_cheese = 10
amount_of_crackers = 50
# Call the function with the variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# Call the function with expressions that add numbers as arguments
cheese_and_crackers(10 + 20, 5 + 6)



print("And we can combine the two, variables and math:")
# Call the function with expressions that add variables and numbers as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
