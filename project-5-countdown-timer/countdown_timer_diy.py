import time

def set_countdown(seconds):
    """
    A generator function that yields the countdown status.
    """
    # 1. Yield a starting message.
    #    Example: "Countdown starts now..."

    # 2. Use a `for` loop to count down from the given `seconds` to 1.
    #    The `range()` function with a step of -1 will be useful here.
    #    `range(start, stop, step)`

    # 3. Inside the loop:
    #    a. Yield the current second as a formatted string (e.g., f'{i:02d}').
    #    b. Use `time.sleep(1)` to pause for one second.

    # 4. After the loop, yield a final message.
    #    Example: "Countdown ended!"
    pass # Remove this line and add your code here

if __name__ == "__main__":
    # 5. Print a welcome message.

    # 6. Start a `while True` loop to allow multiple countdowns.

        # 7. Ask the user if they want to set a countdown (y/n).

        # 8. If 'y', prompt for the number of seconds.
        #    a. Use a `try-except` block to ensure the input is a valid integer.
        #    b. Create a generator object by calling `set_countdown()`.
        #    c. Loop through the generator and print each message it yields.
        #       `for msg in set_countdown(seconds): print(msg)`

        # 9. If 'n', print an exit message and `break` the loop.

        # 10. Handle invalid 'y'/'n' input.
    pass # Remove this line and implement the CLI.
