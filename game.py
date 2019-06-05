#game .py

import random

print("-----------------------------")
print("Rock, Paper, Scissors, Shoot!")
print("-----------------------------")

options = ["rock", "paper", "scissors"]

choice = input("Let's play a game! Select rock, paper or scissors: ") # user input

if choice in options:
    print("-----------------------------")
    print ("You chose:", choice)   
else:
    raise ValueError("OOPS - please type 'rock', 'paper' or 'scissors'.") # error checking

computer = random.choice(options) # computer selects option
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
    print("Keep going")
    
print("-----------------------------")
print("Thanks for playing! Please play again")

