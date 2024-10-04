# I know I have to implement random so that the computer picks a random move.
import random

# Using a list to store all the moves the computer can play
moves = ["R", "P", "S"]

# Choice method will choose a random "move" from the list.
comp_move = random.choice(moves)

# Decorative text
print("PLAY ROCK PAPER SCISSORS AGAINST A COMPUTER! SEE IF YOU CAN WIN!")

# User plays.
user_move1 = input("Press R to play rock. Press P to play paper. Press S to play scissors. ")

if user_move1 == "R":
    if comp_move == "R":
        print("Computer played rock. Tie!")
    elif comp_move == "P":
        print("Computer played paper. Computer wins!")
    elif comp_move == "S":
        print("Computer played scissors. You win!")

elif user_move1 == "P":
    if comp_move == "R":
        print("Computer played rock. You win!")
    elif comp_move == "P":
        print("Computer played paper. Tie!")
    elif comp_move == "S":
        print("Computer played scissors. Computer wins!")

elif user_move1 == "S":
    if comp_move == "R":
        print("Computer played rock. Computer wins!")
    elif comp_move == "P":
        print("Computer played paper. You win!")
    elif comp_move == "S":
        print("Computer played scissors. Tie!")


