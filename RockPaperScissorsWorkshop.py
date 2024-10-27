import random
from random import randrange
print()
print()
print("\t\t\t\tRock . Paper . Scissors".upper())
print()
user_points = 0    #Points Scored by the User
computer_points = 0    #Points Scored by the Computer

while True: 
    print()

    users_choice = input("Enter r for Rock \t Enter p for Paper \t Enter s for Scissors \t Enter q to Quit : ").lower()
    print()
    choice = ["Rock" , "Paper", "Scissors"]


    if not(users_choice == "r" or users_choice == "p" or users_choice == "s" or users_choice == "q"): 
        print("Invalid Input")
        print()    #The block is executed if the input is not the desired one
        continue
    elif users_choice == "q" : 
        print()
        print("RESULTS: ")
        print("")                       #Printing the Results of the Game
        print("COMPUTER'S SCORE = " + str(computer_points))
        print("USER'S SCORE = " + str(user_points))
        print()
        print("The Winner is : ",end="")
        if computer_points > user_points : 
            print("COMPUTER ...!")
            print("Won by " + str(computer_points - user_points) +" points.")
        elif computer_points == user_points: 
            print("Equal Score, Tie. ")
            print("Nobody Wins ...!")
            print()
        else: 
            print("USER ..!")
        break


    computers_choice = randrange(0,3)    #Randomizing a choice for Computer
    print()
    print("Computer's Choice : " + choice[computers_choice])
    print()


        #Condition Checking
    if users_choice == ((choice[computers_choice])[0]).lower() : 
        print("User and Computer has Same Choice, Tie")
        print()
        continue
    if users_choice == "r" and computers_choice == 2 : 
        print("User Wins !")
        user_points += 1
        print()
    elif users_choice == "p" and computers_choice == 0: 
        print("User Wins !")
        user_points += 1
        print()
    elif users_choice == "s" and computers_choice == 1: 
        print("User Wins !")
        user_points += 1
        print()
    else: 
        print("Computer Wins !")
        computer_points += 1
        print()
print()
print()        

    


