import string
import getpass # To hide password input

def check_password_strength(password):
    """
    Analyzes the password and returns a detailed strength report.
    """
    # 1. Initialize counters for different character types to zero.
    #    - lower_alpha_count, upper_alpha_count, number_count,
    #    - whitespace_count, special_char_count

    # 2. Loop through each character of the `password`.
    #    - Use `string.ascii_lowercase`, `string.ascii_uppercase`, etc.,
    #      to check the type of each character and increment the respective counter.

    # 3. Calculate the `strength` score.
    #    - Start with `strength = 0`.
    #    - Add 1 to `strength` for each character type found (e.g., if lower_alpha_count > 0).

    # 4. Determine `remarks` based on the `strength` score.
    #    - Use an if-elif-else chain to assign feedback messages for scores 1 through 5.

    # 5. Build the final `result` string.
    #    - Include the counts of each character type.
    #    - Include the final password score (e.g., "Password score: {strength}/5").
    #    - Include the remarks.

    # 6. Return the `result` string.
    pass # Remove this line and add your code here

if __name__ == "__main__":
    # 7. Print a welcome message.

    # 8. Start a `while True` loop.

        # 9. Ask the user if they want to check a password's strength (y/n).

        # 10. If 'y', use `getpass.getpass()` to securely get the password input.
        #     This hides the password as the user types.

        # 11. Call `check_password_strength()` with the entered password.

        # 12. Print the returned result.

        # 13. If 'n', print an exit message and `break` the loop.

        # 14. Handle invalid 'y'/'n' input.
    pass # Remove this line and implement the CLI.
