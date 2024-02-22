quiz_questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal in the world?": "Blue Whale",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the square root of 64?": "8"
}

def quiz():
    score = 0
    total_questions = len(quiz_questions)

    for question, correct_answer in quiz_questions.items():
        user_answer = input(question + "\nYour answer: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")

    print(f"Quiz complete! You got {score} out of {total_questions} questions correct.")

if __name__ == "__main__":
    quiz()