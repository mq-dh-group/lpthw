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
    Are you ready (yes/no)? Note:
    \tAll options will be presented in the above style.
    \tOptions are spelling and case sensitive. Type exactly one of the options given above.
    \tIf you do not type an option exaclty how it is spelt, you will return to the start of the room.
    \tIf at anytime you want to exit, just press control+C
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
        open_day_room()
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


def open_day_room():
    print("Wow, it's a nice day outside.")
    print('"I\'ll go for a walk. Where to?"')
    print('"Should I go to Le 76 and get a coffee? Or should I just wander with no destination?"')
    print("(coffee/wander)\n")

    action = input ("> ")
    if action == "coffee":
        print('"I\'ll order a capuccino."')
        print('"Well, might as well head back now."')
        print("You fell into the trap of the known. You are now back in the same place as before.")
        nest_room()
    elif action == "wander":
        print("You start to head towards the general direction of the sea.")
        print('"I really think I need to do something. Go somewhere."')
        print("You reach the ocean and start contemplating.")
        print('"That\'s it. I\'m going to the airport tonight and booking a ticket somewhere."')
        airport_room()
    else:
        open_day_room()


def open_night_room():
    print('"I\'ll go for a walk."')
    print("You start to head towards the general direction of the sea.")
    print('"I really think I need to do something. Go somewhere."')
    print("You reach the ocean and start contemplating.")
    print('"That\'s it. I\'m going to the airport tonight and booking a ticket somewhere."')
    print("On the way back you encounter a Silhouette.")
    print('"What is that? Is this a bad sign? Should I still go to the airport?"')
    print("(yes/no)")

    action = input("> ")
    if action == 'yes':
        airport_room()
    elif action == 'no':
        print("The Silhouette sensed your fear of the unknown and killed you.")
        game_over()
    else:
        open_night_room()


def airport_room():
    print("You arrive at international departures. You look for flights departing tonight.")
    print('"That\'s it! I\'ll go there.')
    print("A Crowd of Businessmen pass you by, and it causes you to question your decision")
    print('"Am I escaping reality? Should I really go through with this."')
    print("(yes/no)")

    action = input ("> ")
    if action == 'yes':
        print("You buy a ticket.")
        print("Your plane leaves in 30 minutes. Better get going to the terminal.")
        terminal_room()
    elif action == 'no':
        print("The Pressure gets to you.")
        print("You get home, sleep and awake the next day.")
        nest_room()
    else:
        airport_room()

    
def terminal_room():
    print("Over the loudspeaker you hear: 'Final call!'")
    print('"Well, I guess this is it."')
    print("You get up to board and you get a glimpse of a mean-looking Flight Attendant.")
    print('"I have a bad feeling aboout this. Should I board?"')
    print("(yes/no)")

    action = input("> ")
    if action == 'yes':
        print("Don't judge a book by its cover.")
        print("The Flight Attendant had a lovely nature.")
        plane_room()
    elif action == 'no':
        print("As you leave, the Flight Attendant sees you looking suspicious and calls security.")
        game_over()
    else:
        terminal_room()


def plane_room():
    print("There is nothing here yet.")



start()