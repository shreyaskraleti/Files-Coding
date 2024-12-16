import random
def number_guessing_game():
    print("Welcome to number guessing game!")
    print("I have selected a number between 1 and 100")
    print("can you guess that number")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess:"))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! try again.")
            elif guess > number_to_guess:
                print("Too high! try again.")
            else:
                print(f" Congratulations !!! you have guessed the number in {attempts} attempts. ")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

number_guessing_game()

