import random

# Using a list to store all the moves the computer can play
moves = ["R", "P", "S"]

# Main gameplay loop
running = True

# Decorative text
print("PLAY ROCK PAPER SCISSORS AGAINST A COMPUTER! SEE IF YOU CAN WIN!")
print("----------------------------------------------------------------")

while running:
    # Computer randomly selects a move
    comp_move = random.choice(moves)

    # User plays
    user_move = input("Press R to play rock. Press P to play paper. Press S to play scissors: ").upper()

    print("----------------------------------------------------------------")
    # Print computer and user plays
    print(f"Computer played: {comp_move}")
    print(f"User played: {user_move}")
    print("----------------------------------------------------------------")

    # Decide the outcome
    if comp_move == user_move:
        print("Tie!")

    elif (comp_move == "R" and user_move == "S") or \
            (comp_move == "S" and user_move == "P") or \
            (comp_move == "P" and user_move == "R"):
        print("Computer wins!")

    else:
        print("You win!")

    # Ask if the user wants to play again
    decision = input("Continue playing? Y/N: ").upper()

    if decision == "N":
        running = False
    elif decision != "Y":
        print("Invalid input. Ending game.")
        running = False

print("Game over!")
