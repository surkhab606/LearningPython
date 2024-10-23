grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Please enter the student's name: ")

if student in grades:
    print(f"{student}'s grades are: {grades[student]}")

else:
    print("Student not found.")