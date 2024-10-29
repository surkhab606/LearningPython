import random

word_list = ["rainbow", "strawberry", "games", "dinosaur", "incredible", "uranus"]

comp_word = (random.choice(word_list))
comp_word_length = len(comp_word)

print("You will be given 10 turns to guess letters. After that, you will be prompted to guess the word.")
print(f"The word is {comp_word_length} letters long.")
user_guess = input("Please guess a letter: ")

turns = 10
display_list = []

while turns > 0:
    if user_guess in comp_word:
        print(f"\n{user_guess} is in the word.")
        display_list.append(user_guess)
        print(f"You have successfully guessed the following letters: {display_list}")
        user_guess = input("Please guess another letter: ")
        turns -= 1

    else:
        print(f"\n{user_guess} is not in the word.")
        print(f"You have successfully guessed the following letters: {display_list}")
        user_guess = input("Please guess another letter: ")
        turns -= 1


user_word = input(f"\nYou are out of turns. Please guess the word: ")

if user_word == comp_word:
    print("You got it!")

else:
    print(f"You did not get it. The word was {comp_word}")







if user_guess == comp_word:
        print("You got it!")






