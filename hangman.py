import random

word_list = ["BMW", "UTAHRAPTOR", "CATERPILLAR", "DINOSAUR", "ELEPHANT", "MACBOOK",
             "LESBIAN", "KATE", "CANYON", "ABSOLUTE", "MAXIMUM", "MINIMUM"]

comp_word = random.choice(word_list)
spaces = len(comp_word)

print(f"HANGMAN GAME!")
print(f"The word is {spaces} long.")

hangman = 0

input("Please enter a letter to guess: ")
