print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?
door #1 is more fun.""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear.")
    print("Hint: there is a secret third option.")
    print("Maybe try typing what you actutally should do.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well \"{bear}\" is probably better than the other two options.")
        print("Bear runs away.")
        print("What now?")
        print("1. Go to mid-week beers.")
        print("2. Join #suigang.")

        most_important_decision_of_your_life = input("> ")

        if most_important_decision_of_your_life == "1":
            print("Always the right decision!")
            print("Enjoy yarning with your mates up until 4am probably playing Nidhogg.")
        elif most_important_decision_of_your_life == "2":
            print("A fine choice indeed. But yeh... you're dead now. Game over!")
        else:
            print("There is no secret third option here. You failed. Game over!")


elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
