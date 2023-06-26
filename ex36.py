# This exercise is to create a text game similar to the last exercise.
# The premise: Traversing a plain of obstacles to achieve freedom.
# See ex36_plan.txt for the map of the game

from sys import exit


def start():
    print("""
    Welcome to a simple text game!
    Here you must traverse the life of someone searching for freedom.
    You will traverse across the world and encounter many obstacles. 
    Your choices dictate your ending (there are multiple).
    Remenber. You are trying to achieve freedom!
    Let's get started!
    Are you ready (yes/no)?
    \tNote: all options will presented like above.
    \tOptions are spelling and case sensitive. Type exactly one of the options given.
    \tIf you want to exit. Just press control+C
    """)
    
    choice = input("> ")
    if choice == "yes":
        nest_room()
    elif choice == "no":
        print("Well then why are you here? Come back when you want to play")
        exit(0)
    else:
        print("That's not one of the options I gave you. Type 'yes' or 'no'")
        start()


def game_over():
    print("\nGame over! Thanks for playing :)\n")
    exit(0)


def nest_room():
    print("\nYou are sitting in your apartment one afternoon.")
    print("Your mind starts to wander.")
    print('"I need something new to happen in my life. I need an adventure."')
    print('"Should I get out of here?"')
    print("(no/leave/wait)\n")

    action = input ("> ")
    if action == "leave":
        open_night_room()
    elif action == "wait":
        print("\nIt starts to get dark outside.")
        print("Should I go now?")
        print("(leave/no)\n")
        action = input ("> ")
        if action == "leave":
            open_night_room()
        elif action == "no":
            print("\nThe Big Scary Nothing killed you.")
            game_over()
    elif action == "no":
        print("\nThe Big Scary Nothing killed you.")
        game_over()
    else:
        nest_room()


def open_night_room():
    print("There is nothing here yet.")


def open_day_room():
    print("There is nothing here yet.")


start()