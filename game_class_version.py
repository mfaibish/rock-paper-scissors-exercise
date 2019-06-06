#game_class_version.py

import random

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors': ")
print("-----------")
print("USER  CHOICE: ",user_choice)

# VALIDATE INPUTS

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()

# GENERATE CONPUTER SELECTION

computer_choice = random.choice(options)
print("-----------")
print("GENERATING...")
print("COMPUTER CHOICE: ", computer_choice)

# DETERMINE WINNER

#rock beats scissors
#paper beats rock
#scissors beats paper
#same selection is a tie

if user_choice == computer_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "paper":
    print("WINNER: paper")
    print("COMPUTER WINS")
elif user_choice =="rock" and computer_choice == "scissors":
    print("WINNER: rock")
    print("YOU WIN")
elif user_choice == "paper" and computer_choice == "rock":
    print("WINNER: paper")
    print("YOU WIN")
elif user_choice =="paper" and computer_choice == "scissors":
    print("WINNER: scissors")
    print("COMPUTER WINS")
elif user_choice == "scissors" and computer_choice == "paper":
    print("WINNER: scissors")
    print("YOU WIN")
elif user_choice =="scissors" and computer_choice == "rock":
    print("WINNER: rock")
    print("COMPUTER WINS")

print("-----------")
# DISPLAY FINAL OUTPUTS / OUTCOMES