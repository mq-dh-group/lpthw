def introScene():
  # This function defines the introduction scene of your game.
  # It prints some text to describe the scene and asks the player to choose a direction to go.
  # It also checks if the player's input is valid and calls the next scene accordingly.

  # Use print statements to display text to the player.
  # A print statement uses the print keyword, followed by parentheses that enclose the text to be printed.
  # You can use quotation marks to indicate a string, which is a sequence of characters.
  # You can also use escape characters like \n to add special effects, such as a new line.

  print("You are standing in front of a large wooden door.\n")
  print("There is a sign that says 'Welcome to the Python Dungeon'.\n")
  print("You wonder what lies behind the door.\n")

  # Use input statements to get text from the player.
  # An input statement uses the input keyword, followed by parentheses that enclose a prompt for the player.
  # The input statement will wait for the player to type something and press enter, and then return what they typed as a string.
  # You can assign the return value of an input statement to a variable using the = operator.
  # A variable is a name that refers to a value stored in memory.

  direction = input("Do you want to enter the door? (yes/no) ")

  # Use if statements to make decisions based on conditions.
  # An if statement uses the if keyword, followed by parentheses that enclose a condition to be evaluated.
  # A condition is an expression that can be either True or False, such as comparing two values using operators like == (equal) or != (not equal).
  # After the parentheses, you add a colon and then indent the next line to start the if block.
  # The if block contains the code that will be executed if the condition is True.
  # You can also use elif (short for else if) and else keywords to add more branches to your if statement, with their own conditions and blocks.

  if direction == "yes":
    # If the player typed "yes", call the next scene function using its name and parentheses.
    doorScene()
  elif direction == "no":
    # If the player typed "no", print a message and end the game using the exit() function.
    print("You decide not to enter the door.\n")
    print("You turn around and walk away.\n")
    print("Game over.\n")
    exit()
  else:
    # If the player typed anything else, print an error message and call the same scene function again to repeat the choice.
    print("Invalid input. Please type yes or no.\n")
    introScene()

def doorScene():
  # This function defines another scene of your game, where the player enters the door and finds a hallway with two doors.
  # It follows the same structure as the introScene function, but with different text and choices.

  print("You enter the door and find yourself in a dark hallway.\n")
  print("There are two doors on each side of the hallway.\n")
  print("One is red and one is blue.\n")

  direction = input("Which door do you want to open? (red/blue) ")

  if direction == "red":
    redDoorScene()
  elif direction == "blue":
    blueDoorScene()
  else:
    print("Invalid input. Please type red or blue.\n")
    doorScene()

def redDoorScene():
  # This function defines another scene of your game, where the player opens the red door and finds a treasure chest.
  # It follows the same structure as the previous functions, but with different text and choices.

  print("You open the red door and find a treasure chest.\n")
  print("It is locked with a combination lock.\n")
  print("There are three dials, each with numbers from 0 to 9.\n")

  # You can use the + operator to concatenate strings, which means joining them together.
  # You can also use the str() function to convert other types of values, such as numbers, to strings.

  combination = "123" # This is the correct combination. You can change it to anything you want.
  attempt = input("Enter the combination (3 digits): ") # Ask the player to enter a 3-digit number.

  if attempt == combination:
    print("You enter the combination and hear a click.\n")
    print("You open the chest and find a golden key.\n")
    print("You win!\n")
    exit()
  else:
    print("You enter the wrong combination and hear a loud alarm.\n")
    print("The door slams shut and locks behind you.\n")
    print("You are trapped.\n")
    print("Game over.\n")
    exit()

def blueDoorScene():
  # This function defines another scene of your game, where the player opens the blue door and finds a monster.
  # It follows the same structure as the previous functions, but with different text and choices.

  print("You open the blue door and find a monster.\n")
  print("It is a huge python snake that hisses at you.\n")
  print("You have two options: fight or run.\n")

  action = input("What do you want to do? (fight/run) ")

  if action == "fight":
    print("You decide to fight the monster.\n")
    print("You grab a nearby stick and swing it at the snake.\n")
    print("The snake dodges your attack and bites you.\n")
    print("You feel a burning sensation in your veins.\n")
    print("You are poisoned.\n")
    print("Game over.\n")
    exit()
  elif action == "run":
    print("You decide to run away from the monster.\n")
    print("You sprint back to the hallway and slam the door behind you.\n")
    print("You are safe for now.\n")

    # You can use variables to store information that can change during the game, such as the player's inventory or health.
    # You can also use boolean values (True or False) to indicate the state of something, such as whether a door is locked or not.
    # You can use these variables in your conditions to create more complex logic for your game.

    blueDoorLocked = True # This variable indicates whether the blue door is locked or not. Initially, it is set to True.

    if blueDoorLocked == True:
      # If the blue door is locked, print a message and call another scene function.
      print("However, you notice that the blue door is locked from the inside.\n")
      print("You have no choice but to open the red door.\n")
      redDoorScene()
    else:
      # If the blue door is not locked, print a message and call another scene function.
      # You can use this branch to create an alternative path for your game, such as finding a key to unlock the blue door later.
      print("However, you notice that the blue door is unlocked from the inside.\n")
      print("You have a choice: open the red door or go back to the blue door.\n")
      someOtherScene()
  else:
    print("Invalid input. Please type fight or run.\n")
    blueDoorScene()

# Define any other scene functions that you want for your game here.

# Define a main function that will start your game when you run this file.
# The main function will contain some introductory text and call the first scene function of your game.

def main():
  print("Welcome to Python Dungeon!\n")