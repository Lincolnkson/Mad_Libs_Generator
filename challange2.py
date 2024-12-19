import random

print("Welcome to the Number Guessing Game!")

# Main game loop
while True:
    # Generate the secret number
    secret_number = random.randint(1, 10)
    print("\nI'm thinking of a number between 1 and 10. Can you guess it?")
    
    guess_count = 0  # Counter for guesses
    
    # Inner guessing loop
    while True:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        guess_count += 1
        
        # Match-case block for checking the guess
        match (guess):
            case x if x == secret_number:
                print(f"🎉 Congratulations, you guessed it in {guess_count} guesses!")
                break
            case x if x > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case x if x < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
    
    # Ask if the user wants to play again
    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break