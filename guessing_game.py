#!  /usr/bin/python3

# The random package is needed to choose a random number
import random

# Define the game in a function
def guess_loop():
    # Define a counter for wrong guesses
    count = 5
    # Ask to the user his name
    name = input("Hello, user ! Would you please enter your name, please ?\n")
    if isinstance(name, str) :
        name = input("That does not seem to be a name. Please redo.\n")

    # This is the number the user will have to guess , chosen randomly
    # in between 1 and 100
    number_to_guess = random.randint (1 , 100)
    print ("I have in mind a number in between 1 and 100 , can you find it in 5 trials ?")
    # Replay the question until the user finds the correct number
    while True :
        try :
            if count != 0 :
                # Read the number the user inputs
                guess = int(input())
                # Compare it to the number to guess
                if guess > number_to_guess :
                    print ("The number to guess is lower. {:d} trials remaining".format(count-1))
                    count -=1
                elif guess < number_to_guess :
                    print ("The number to guess is higher. {:d} trials remaining".format(count-1))
                    count -=1
                else :
                # The user found the number to guess , let ’s exit
                    print ("Well done, {:s} ! You just found the number, it was indeed {:d}.".format(name, guess))
                    return
            else :
                print("Sorry, you have used your 5 tries.")
                break
        # A ValueError is raised by the int() function if the user inputs something else than a number
        except ValueError :
            print ("Invalid input , please enter an integer")

# Launch the game
guess_loop()