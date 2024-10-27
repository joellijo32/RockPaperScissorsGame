import random
from random import randrange

print("\n\n\t\t\t\tRock . Paper . Scissors\n".upper())

user_points = 0    #Points Scored by the User
computer_points = 0    #Points Scored by the Computer

while True: 
    

    users_choice = input("\nEnter r for Rock \t Enter p for Paper \t Enter s for Scissors \t Enter q to Quit : \n").lower()
    
    choice = ["Rock" , "Paper", "Scissors"]


    if not(users_choice == "r" or users_choice == "p" or users_choice == "s" or users_choice == "q"): 
        print("Invalid Input\n")
            #The block is executed if the input is not the desired one
        continue
    elif users_choice == "q" : 
        
        print("\nRESULTS: \n")
                               #Printing the Results of the Game
        print("COMPUTER'S SCORE = " + str(computer_points)+"\n")
        print("USER'S SCORE = " + str(user_points) +"\n")
        
        print("The Winner is : ",end="")
        if computer_points > user_points : 
            print("COMPUTER ...!")
            print("Won by " + str(computer_points - user_points) +" point(s) .\n")
        elif computer_points == user_points: 
            print("Equal Score, Tie. ")
            print("Nobody Wins ...!\n")
            
        else: 
            print("USER ..!")
        break


    computers_choice = randrange(0,3)    #Randomizing a choice for Computer
    
    print("\nComputer's Choice :  " + choice[computers_choice])
    


        #Condition Checking
    if users_choice == ((choice[computers_choice])[0]).lower() : 
        print("\nUser and Computer has Same Choice, Tie\n\n\n")
        
        continue
    if users_choice == "r" and computers_choice == 2 : 
        print("\nUser Wins !\n\n\n")
        user_points += 1
       
    elif users_choice == "p" and computers_choice == 0: 
        print("\nUser Wins !\n\n\n")
        user_points += 1
        
    elif users_choice == "s" and computers_choice == 1: 
        print("\nUser Wins !\n\n\n")
        user_points += 1
        
    else: 
        print("\nComputer Wins !\n\n\n")
        computer_points += 1
        
        

    


