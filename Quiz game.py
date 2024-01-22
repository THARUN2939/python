questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?",
]

answers = [
    "Paris",
    "Leonardo da Vinci",
    "Jupiter",
    "Au",
]

score = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")

    if user_answer.lower() == answers[i].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

print("Quiz completed!")
print("Your score:", score, "out of", len(questions))
