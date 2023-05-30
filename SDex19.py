# Study drill 3. for ex19.py
# Write at least one more function of your own design, and run it 10 different ways.

# I'm writing a function that turns a percentage or decimal into a sabemetric style format (i.e., to three decimal places)
# Written by Austin with assistance from Bing Chat.


def sabermetric_conversion(percent):
    print(f"\tLet's take your {percent} and make it sabemetric!")
    # check the type of the input
    if type(percent) == str:
        # if it is a string, remove the '%' sign if present
        percent = percent.replace('%', '')
    float_value = float(percent) / 100
    # format the float so that it has 3 decimal places
    float_value = f'{float_value:.3f}'
    # print the float_value as a string
    print(f"\tYour sabemetric number is {float_value}\n")

# Call the function with a string as an argument
print("Someone told me that Lamont Wade Jr's gets on base 43.4% of the time. So, what is his on base average?")
sabermetric_conversion('43.4%')


print("What would his on base average be if he got on base 10% more often?")
print("We need to add 10 to 43.4, which is 53.4.")
Lamonts_OBP = 43.4
# Call the function with expressions that add a variable and a number as an argument
sabermetric_conversion(Lamonts_OBP + 10)


print("Let's try another one.")
print("What percent of the time did you get a hit in college?")
user_BA = input()
# Call the function with a variable that is defined by user input
sabermetric_conversion(user_BA)

print("When someone says a player has an OPS of over one thousand, what does that look like?")
print('You might here someone say, "Aaron Judge has an OPS of over one thousand, or that "he has a whopping one dot one one one OPS"')
print("Aaron Judge's OPS is calculated by combining his OBP (.425) and SLG (.686)")
sabermetric_conversion(42.5 + 68.6)
