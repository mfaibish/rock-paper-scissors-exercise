# game.py

import random

def my_message():
    return "HELLO"

def determine_winner(user_choice, comp_choice):
    winners = {
    "rock":{
        "rock": None,
        "paper": "paper",
        "scissors": "rock",
    },
    "paper":{
        "rock": "paper",
        "paper": None,
        "scissors": "scissors",
    },
    "scissors":{
        "rock": "rock",
        "paper": "scissors",
        "scissors": None,
        },
    }
    winning_choice = winners[user_choice][comp_choice]
    return winning_choice

# only if this script is executed from the command line
if __name__ == "__main__":

    print("Rock, Paper, Scissors, Shoot!") # this is also a comment

    # CAPTURE INPUTS

    user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

    print("--------------")
    print("USER CHOICE:", user_choice)

    # VALIDATE INPUTS

    options = ["rock", "paper", "scissors"]

    if user_choice not in options:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
        exit()

    # GENERATE COMPUTER SELECTION

    computer_choice = random.choice(options)

    print("--------------")
    print("GENERATING...")
    print("COMPUTER CHOICE:", computer_choice)

    # DETERMINE THE WINNER
    #
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    # same selections is a tie
    #
    # first attribute represents the user, second represents the computer
    
    winning_choice = determine_winner(user_choice, computer_choice)

    # DISPLAY FINAL OUTPUTS / OUTCOMES

    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
        print("TIE")

    print("Thanks for playing. Please play again!")