# Import the random module for generating random numbers
import random

# Define a function named generate_powerball_numbers
def generate_powerball_numbers():
    # Print a welcome message to the user
    print("Welcome to the Powerball number generator!")

    # Start an infinite loop
    while True:
        # Prompt the user to enter 'yes' or 'no', convert input to lowercase, and store it in user_input
        user_input = input("Do you want Powerball numbers? (yes/no): ").lower()

        # Check if the user entered 'no'
        if user_input == 'no':
            # Print a goodbye message and break out of the loop
            print("Goodbye!")
            break

        # Check if the user entered 'yes'
        elif user_input == 'yes':
            # Generate a list of 5 unique random numbers between 1 and 69 (inclusive)
            white_numbers = random.sample(range(1, 70), 5)

            # Generate a single random number between 1 and 26 (inclusive)
            red_number = random.randint(1, 26)

            # Print the generated Powerball numbers to the user
            print("Your Powerball numbers are:")
            print("White numbers:", white_numbers)
            print("Red number:", red_number)

        # If the user input is neither 'yes' nor 'no', print an error message
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the generate_powerball_numbers function
    generate_powerball_numbers()