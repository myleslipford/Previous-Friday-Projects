# Previous-Friday-Projects

Notes for FridayProject1.py

1. Function Definition (def madlib():): Defines a function named madlib.

2. Madlib Template (template = "..."): Stores the madlib story template with placeholders in a variable named template.

3. User Input (adjective = input("Enter an adjective: ")): Prompts the user to enter an adjective and stores the input in the variable adjective. The same process is repeated for the other input variables (large_object_plural, body_part, restaurant, food, another_food).

5. Replace Placeholders (madlib_story = template.format(...)): Replaces the placeholders in the template with the user-provided input using the format method and stores the result in the variable madlib_story.

6. Print the Completed Madlib Story (print(madlib_story)): Prints the completed madlib story to the console.

7. Call the Madlib Function (madlib()): Invokes the madlib function, initiating the madlib program and executing the code within the function.




Notes for FridayProject2.py

1. Import the random module for generating random numbers.
   `import random`

2. Define a function named `generate_powerball_numbers`.
   `def generate_powerball_numbers():`

3. Print a welcome message to the user.
   `print("Welcome to the Powerball number generator!")`

4. Start an infinite loop to repeatedly ask the user for input.
   `while True:`

5. Prompt the user to enter 'yes' or 'no', convert input to lowercase, and store it in `user_input`.
   `user_input = input("Do you want Powerball numbers? (yes/no): ").lower()`

6. Check if the user entered 'no'.
   `if user_input == 'no':`

7. Print a goodbye message and break out of the loop if the user entered 'no'.
   `print("Goodbye!")`
   `break`

8. Check if the user entered 'yes'.
   `elif user_input == 'yes':`

9. Generate a list of 5 unique random numbers between 1 and 69 (inclusive) for the white balls.
   `white_numbers = random.sample(range(1, 70), 5)`

10. Generate a single random number between 1 and 26 (inclusive) for the red Powerball.
    `red_number = random.randint(1, 26)`

11. Print the generated Powerball numbers to the user.
    `print("Your Powerball numbers are:")`
    `print("White numbers:", white_numbers)`
    `print("Red number:", red_number)`

12. If the user input is neither 'yes' nor 'no', print an error message.
    `else:`
    `print("Invalid input. Please enter 'yes' or 'no'.")`

13. Check if the script is being run as the main program.
    `if __name__ == "__main__":`

14. Call the `generate_powerball_numbers` function if the script is the main program.
    `generate_powerball_numbers()`




Notes For Fridayproject3.py

1. `quiz_questions = { ... }`: Defines a dictionary containing quiz questions as keys and correct answers as values.

2. `def quiz():`: Defines a function named 'quiz' to encapsulate the quiz logic.

3. `score = 0`: Initializes a variable to keep track of the user's score.

4. `total_questions = len(quiz_questions)`: Calculates the total number of questions in the quiz.

5. `for question, correct_answer in quiz_questions.items():`: Iterates through each question and correct answer in the quiz dictionary.

6. `user_answer = input(question + "\nYour answer: ")`: Asks the user for input, displaying the current question.

7. `if user_answer.lower() == correct_answer.lower():`: Checks if the user's answer (case-insensitive) matches the correct answer.

8. `print("Correct!\n")`: Prints a message indicating that the answer is correct.

9. `score += 1`: Increments the user's score.

10. `else:`: Handles the case when the user's answer is incorrect.

11. `print(f"Wrong! The correct answer is: {correct_answer}\n")`: Prints a message indicating that the answer is wrong and displays the correct answer.

12. `print(f"Quiz complete! You got {score} out of {total_questions} questions correct.")`: Displays the user's final score after completing the quiz.

13. `if __name__ == "__main__":`: Checks if the script is executed as the main program.

14. `quiz()`: Calls the 'quiz' function to start the quiz when the script is run.
