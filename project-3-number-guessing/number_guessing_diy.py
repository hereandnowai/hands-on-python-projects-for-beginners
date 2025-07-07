import random

# 1. Generate a random secret number between 0 and 9.
#    Store it in a global variable `secret_number`.
secret_number = 0 # Replace this with a call to random.randint()

def make_guess(user_guess):
    """
    Compares the user's guess with the secret number and returns feedback.
    """
    global secret_number
    # 2. Check if `user_guess` is equal to `secret_number`.
    #    If it is, the user won.
    #    a. Generate a new `secret_number` for the next game.
    #    b. Return a winning message, e.g., "Correct! You win! Guess again!"

    # 3. If the guess is not correct, check if it's less than the secret number.
    #    If so, return a hint to guess higher, e.g., "Enter a higher number!".

    # 4. Otherwise, the guess must be greater than the secret number.
    #    Return a hint to guess lower, e.g., "Enter a lower number!".
    pass # Remove this line and add your code here

if __name__ == "__main__":
    # 5. Print a welcome message and instructions.
    #    Example: "Guess a number between 0 and 9!"

    # 6. Start an infinite `while True:` loop to handle guesses.

        # 7. Use a `try-except` block to handle potential `ValueError`.
        #    This prevents the program from crashing if the user enters non-numeric input.

            # 8. Inside the `try` block, get the user's guess using `input()`.
            #    Convert it to an integer.

            # 9. Call the `make_guess()` function with the user's number.
            #    Store the returned feedback in a variable.

            # 10. Print the feedback to the user.

            # 11. If the feedback contains the word "Correct!", the user has won.
            #     Use the `break` keyword to exit the loop.

        # 12. In the `except ValueError` block, print an error message.
        #     Example: "Invalid input. Please enter a number."
        pass # Remove this line and implement the steps above.
