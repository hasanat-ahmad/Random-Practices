def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for i, (question, answer) in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question}")
        user_answer = input("Your answer: ").lower()

        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"\nQuiz complete! You scored {score}/{total_questions}.")

def main():
    print("Simple Quiz Game")

    quiz_questions = [
        ("What is the capital of France?", "Paris"),
        ("Which planet is known as the Red Planet?", "Mars"),
        ("What is the largest mammal?", "Blue Whale"),
        ("How many continents are there?", "7"),
        ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ]

    run_quiz(quiz_questions)

if __name__ == "__main__":
    main()
