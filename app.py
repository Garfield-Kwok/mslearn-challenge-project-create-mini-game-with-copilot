# i want to create a mini game 
# The winner of the game is determined by three simple rules:
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# Game interaction considerations
# The computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors). Your game interaction will be through the console (Terminal).

# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# The game must be able to handle ties and inform the user if they won or lost.


# import random module

import random

# create a list of play options
options = ["rock", "paper", "scissors"]

# assign a random play to the computer
computer = random.choice(options)

# set player to False
player = False

# initialize player's score
score = 0

while player == False:
    # set player to True
    player = input("Choose rock, paper or scissors: ")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
            # increment player's score
            score += 1
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
            # increment player's score
            score += 1
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
            # increment player's score
            score += 1
    else:
        print("Invalid input. Please try again.")

    player = input("Do you want to play again? (y/n): ")
    if player == "y":
        player = False
        computer = random.choice(options)
    else:
        print("Thanks for playing!")
        break

# display player's score at the end of the game
print("Your score:", score)




