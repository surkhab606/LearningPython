import random

word_list = ["BMW", "UTAHRAPTOR", "CATERPILLAR", "DINOSAUR", "ELEPHANT", "MACBOOK",
             "LESBIAN", "KATE", "CANYON", "ABSOLUTE", "MAXIMUM", "MINIMUM"]

comp_word = random.choice(word_list)
spaces = len(comp_word)
guess_list = list(comp_word)
placeholder = ['_'] * len(comp_word)

print(f"HANGMAN GAME!")
print(f"The word is {spaces} letters long.")

hangman = 0

user_guess = input("Please enter a letter to guess: ").upper()


for index, letter in enumerate(comp_word):
    if letter == user_guess:
        placeholder[index] = user_guess

print("Current progress:", ' '.join(placeholder))





