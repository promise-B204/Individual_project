# List of questions, answers, and options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Shakespeare", "B) Dickens", "C) Tolstoy", "D) Austen"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    }
]


PASS_MARK = 3  # 3 out of 4 correct answer


def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)


def get_answer():
    while True:
        answer = input("Please select your answer (A, B, C, or D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid choice. Please select A, B, C, or D.")


def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return 1  # Correct answer
    else:
        return 0  # Incorrect answer


def run_quiz(questions):
    score = 0

    for question_data in questions:
        display_question(question_data)
        user_answer = get_answer()
        score += evaluate_answer(user_answer, question_data["answer"])

    return score


def display_result(score):
    print(f"\nYour total score: {score}/{len(questions)}")

    if score >= PASS_MARK:
        print("Congratulations! You passed the quiz!")
    else:
        print("Sorry, you failed the quiz. Better luck next time.")

# Main function to execute the quiz


def main():
    print("Welcome to the Quiz! Let's begin.\n")
    score = run_quiz(questions)
    display_result(score)


if __name__ == "__main__":
    main()
