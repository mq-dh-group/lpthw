from sys import argv

script, user_name = argv
prompt = 'go on... tell me: '
prompt_2 = 'I won\'t share this information I swear, but do tell me: '
prompt_3 = 'I must know, tell me: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt_2)

print("What kind of computer do you have?")
computer = input(prompt_3)

print(f'''
Alright, so you said "{likes}" about liking me.
You live in "{lives}". Not sure where that is.
And you have a "{computer}" computer. Nice.
''')