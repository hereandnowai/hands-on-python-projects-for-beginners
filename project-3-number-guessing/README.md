# Project-Based Python: A Beginner's Guide to Building a Number Guessing Game

**Welcome!** In this lesson, we will learn the fundamentals of Python programming by building a functional number guessing game. We'll start with a simple command-line version and then create a web-based user interface for it. Every concept you learn will be something you immediately see and use in our project.

---

## Part 1: The Game's Brain (`number_guessing.py`)

This first file contains all the core logic for our number guessing game.

#### 1. Importing the `random` Module
To make our game unpredictable, we need to generate a random number. Python's built-in `random` module is perfect for this.

*   **In the code:**
    ```python
    import random
    ```

#### 2. Defining Functions: Creating Reusable Code
A function is a named, reusable block of code that performs a specific action. We use the `def` keyword to create one.

*   **`get_random_number()`**: This function generates the secret number the user needs to guess.
    *   **In the code:**
        ```python
        def get_random_number():
            return random.randint(0, 9)
        ```
        *   **`random.randint(0, 9)`**: Returns a random integer between 0 and 9 (inclusive).

*   **`check_guess(user_guess, secret_number)`**: This function compares the user's guess to the secret number and provides feedback.
    *   **In the code:**
        ```python
        def check_guess(user_guess, secret_number):
            if user_guess == secret_number:
                return "Correct! You win!", True
            elif user_guess < secret_number:
                return "Too low!", False
            else:
                return "Too high!", False
        ```
    *   It returns two values: a `message` (feedback to the user) and a `boolean` (`True` if the game is over, `False` otherwise).

#### 3. The Main Execution Block: `if __name__ == "__main__":`
This is a special, standard Python construct. The code inside this block only runs when you execute the file directly from the terminal. It won't run if this file is imported into another file (like our UI file does!).

*   **In the code:**
    ```python
    if __name__ == "__main__":
        # All the code indented below here runs at the start.
    ```

#### 4. Loops: Repeating Actions with `while`
A `while` loop will repeat the code inside it as long as its condition is `True`.

*   **In the code:**
    ```python
    while True:
        # ... code to ask for input and check guess ...
    ```
    *   **`while True:`**: This creates an infinite loop. We need a way to get out!
    *   **`break`**: The `break` keyword immediately exits the current loop. We use it to stop the game when the user guesses correctly.

#### 5. User Interaction: `print()`, `input()`, and Data Types
*   **`print()`**: Displays text or variables to the user in the console.
*   **`input()`**: Pauses the program, prompts the user with a message, and waits for them to type something and press Enter. It always returns the input as a string (text).
*   **Type Casting with `int()`**: Since `input()` gives us text, we must convert it to an integer (`int()`) before we can compare it with our secret number.

---

## Part 2: The User Interface (`number_guessing_ui.py`)

Now we'll take our game logic and give it a user-friendly graphical interface that can be opened in a web browser.

#### 1. Importing: Using Code from Other Files and Libraries
Importing allows us to use functions and tools from other files or from external packages that other developers have built.

*   **In the code:**
    ```python
    import gradio as gr
    from number_guessing import get_random_number, check_guess
    ```
    *   **`from number_guessing import get_random_number, check_guess`**: This imports our game logic functions from `number_guessing.py`.
    *   **`import gradio as gr`**: This imports the `gradio` library, giving it the alias `gr`.

#### 2. Game State Management
For a UI, we need to keep track of the `secret_number` and `chances` across different user interactions. We use global variables for simplicity in this beginner example.

*   **In the code:**
    ```python
    secret_number = get_random_number()
    chances = 0
    ```

#### 3. The UI Function (`guess_number_ui`)
This function is called by Gradio whenever the user makes a guess. It updates the game state and returns the feedback message.

*   **In the code:**
    ```python
    def guess_number_ui(user_guess):
        global secret_number, chances
        chances += 1
        message, game_over = check_guess(user_guess, secret_number)
        # ... logic to reset game if over ...
        return final_message_or_feedback
    ```

#### 4. Creating the Interface with Gradio
The `gr.Interface` is the main object that creates our web UI. We configure it by telling it what function to use and what the inputs and outputs should look like.

*   **In the code:**
    ```python
    gr.Interface(
        fn=guess_number_ui,
        inputs=gr.Number(label="Enter your guess (0-9)"),
        outputs="text",
        title="Simple Number Guessing Game"
    ).launch()
    ```
    *   **`fn=guess_number_ui`**: Tells Gradio to call our `guess_number_ui` function when the user submits a guess.
    *   **`inputs=gr.Number(...)`**: Defines the input field for the user's guess.
    *   **`outputs="text"`**: Defines the output field where feedback is displayed.
    *   **`.launch()`**: This starts the local web server and makes your game UI available in your browser.