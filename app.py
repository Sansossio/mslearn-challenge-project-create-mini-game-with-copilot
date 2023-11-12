# Let's add some more excitement to this challenge and make the game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

# Generate the code for the game using the template below:

import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    # Write your code below
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    while True:
        player_choice = input("Enter your choice: ").lower()
        computer_choice = random.choice(options)
        if player_choice not in options:
            print("Invalid input. Try again.")
            continue
        print(f"Computer chose {computer_choice}.")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "paper":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        elif player_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            break
    print("Thanks for playing!")

rock_paper_scissors()

# Path: app.py
