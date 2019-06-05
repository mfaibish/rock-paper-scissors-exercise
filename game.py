#game .py

import random


print("-----------------------------")
print("Rock, Paper, Scissors, Shoot!")
print("-----------------------------")
options = ["rock", "paper", "scissors"]
response = "y"
while response == "y":
    choice = input("Let's play a game! Select rock, paper or scissors: ") # user input
    if choice in options:
        print("-----------------------------")
        print ("You chose:", choice)   
    else:
        raise ValueError("OOPS - please type 'rock', 'paper' or 'scissors'.") # error checking

# computer selects option    
    computer = random.choice(options) 
    print("The computer chose:", computer)
    print("-----------------------------")

# logic to return results
    if choice == "rock" and computer == "scissors":
        print("You win!")
    elif choice == "paper" and computer == "rock":
        print ("You win!")
    elif choice == "scissors" and computer == "paper":
        print("You win!")
    elif choice == computer:
        print("It's a tie")
    elif(choice != computer):
        print("You lose")
    print("-----------------------------")
    
    response = input("Do you want to play again? (y/n): " ) 
   

