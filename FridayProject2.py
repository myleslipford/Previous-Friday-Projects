import random

def generate_powerball_numbers():
    print("Welcome to the Powerball number generator!")
    
    while True:
        user_input = input("Do you want Powerball numbers? (yes/no): ").lower()
        
        if user_input == 'no':
            print("Goodbye!")
            break
        elif user_input == 'yes':
            # Generate 5 numbers between 1 and 69
            white_numbers = random.sample(range(1, 70), 5)
            
            # Generate 1 number between 1 and 26
            red_number = random.randint(1, 26)
            
            print("Your Powerball numbers are:")
            print("White numbers:", white_numbers)
            print("Red number:", red_number)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    generate_powerball_numbers()