# Import Statement to get a random number
import random

# Getting a Random Integer
random_number=random.randint(0,100)

# "i" to check if the user finished the game or not ( 0=completing | 1=completed )
i=0

# To check how many tries a player took
tries=1

# Printing a intro statement 
print("Guess a number between 1 to 100.")

# ------------------------------------------------main logic starts

# while loop to repeat the user input
while(i < 1):

    # Printing the try number
    print("Try-->", tries)

    # Taking user Input
    ans = int(input())

    # if statement to check the to check if the player is correct(main if)
    if(ans == random_number):

        # if statement to check  whether completed on first try (inside main if statement)
        if(tries==1):

            # The message to be printed to show the caption of their  play
            msg="Yeah, You nailed that on the first try!!"
            # Used input as a buffer
            completed=input(msg)
        
        # else statement of the above if statement to show the user completed on second or more try (inside main if statement)
        else:

            # The message to be printed to show the caption of their  play
            print("Yeah, You nailed that on",tries,"try!!")
            #  Used input as a buffer
            completed=input()

        # setting i to 1 (because player completed ) (inside main if)
        i=1

        # main else statement to show hints
    else:

        # increaing the try number
        tries=tries+1

        # if statement to show hint if the ans is low 
        if(ans<random_number):
            print("The number is low")

        # elif statement to show hint if the ans is high
        elif(ans>random_number):
            print("The number is high")
