#game_class_version.py

import random

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors': ")
print("-----------")
print("USER  CHOICE: ",user_choice)

# VALIDATE INPUTS

choice = ["rock", "paper", "scissors"]

if user_choice not in choice:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()

# GENERATE CONPUTER SELECTION

computer_choice = random.choice(choice)
print("-----------")
print("GENERATING...")
print("COMPUTER CHOICE: ", computer_choice)

# DETERMINE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES