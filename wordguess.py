import random

word_list = ["rainbow", "strawberry", "games", "dinosaur", "incredible", "uranus"]

comp_word = (random.choice(word_list))

user_guess = input("Please guess the word!: ")


while user_guess != comp_word:
    user_guess = input("Try again!: ")

    if user_guess == comp_word:
        print("You got it!")



