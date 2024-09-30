questions = ("What is the smallest country in the world?",
             "What is the only continent without an active volcano?",
             "Which planet is known as the 'Morning Star' or the 'Evening Star'?",
             "Which planet in our solar system has the most moons?",
             "What is the name of the first satellite sent into space?")

options = (("A. Monaco", "B. Vatican City", "C. San Marino", "D. Liechtenstein"),
           ("A. Africa", "B. Europe", "C. Australia", "D. Antarctica"),
           ("A. Mars", "B. Venus", "C. Mercury", "D. Jupiter"),
           ("A. Jupiter", "B. Saturn", "C. Uranus", "D. Neptune"),
           ("A. Sputnik 1", "B. Explorer 1", "C. Apollo 1", "D. Apollo 10"))

answers = ("B", "C", "B", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-----------------------------------")
print("             RESULTS               ")
print("-----------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")
