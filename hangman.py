import random

word_list = ["BMW", "UTAHRAPTOR", "CATERPILLAR", "DINOSAUR", "ELEPHANT", "MACBOOK",
             "LESBIAN", "KATE", "CANYON", "ABSOLUTE", "MAXIMUM", "MINIMUM"]

comp_word = random.choice(word_list)
spaces = len(comp_word)
placeholder = ['_'] * len(comp_word)

print(f"HANGMAN GAME!")
print(f"The word is {spaces} letters long.")

hangman = 0

while '_' in placeholder and hangman < 6:  # Continue until word is guessed or max tries are reached
    user_guess = input("Please enter a letter to guess: ").upper()

    # Reset the flag to check if the guess is correct in the current round
    guess_correct = False

    # Loop through each letter in the word
    for index, letter in enumerate(comp_word):
        if letter == user_guess:
            placeholder[index] = user_guess
            guess_correct = True  # Update the flag if guess is correct

    # Display current progress if the guess was correct
    if guess_correct:
        print("Current progress:", ' '.join(placeholder))
    else:
        # Increment hangman count if guess was incorrect
        hangman += 1
        print(f"{user_guess} is not in the word. You have {6 - hangman} tries left.")

# End game messages
if '_' not in placeholder:
    print("Congratulations! You've guessed the word:", comp_word)
else:
    print("Game over! The word was:", comp_word)
