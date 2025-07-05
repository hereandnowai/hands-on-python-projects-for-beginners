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

#### 2. Global Variables: Game State
To keep track of the secret number across multiple guesses, we use **global variables**. These variables are defined outside of any function and can be accessed and modified from anywhere in the file.

*   **`secret_number`**: The random number the user needs to guess.
*   **In the code:**
    ```python
    secret_number = random.randint(0, 9)
    ```

#### 3. The `make_guess()` Function: All Game Logic in One Place
This single function handles everything related to a user's guess: comparing it to the secret number, providing feedback, and resetting the game if the guess is correct.

*   **In the code:**
    ```python
    def make_guess(user_guess):
        global secret_number # Tells Python we want to modify the global secret_number
        if user_guess == secret_number:
            secret_number = random.randint(0, 9) # Reset for new game
            return "Correct! You win! Starting a new game..."
        return "Too low!" if user_guess < secret_number else "Too high!"
    ```
    *   **`global secret_number`**: This crucial line tells Python that when we refer to `secret_number` inside this function, we mean the global variable, not a new local one.
    *   **Conditional Logic**: Uses `if`, `elif`, and `else` to check if the guess is correct, too low, or too high.
    *   **Game Reset**: If the guess is correct, a new `secret_number` is generated, effectively starting a new game.

#### 4. The Main Execution Block: `if __name__ == "__main__":`
This is a special, standard Python construct. The code inside this block only runs when you execute the file directly from the terminal. It won't run if this file is imported into another file (like our UI file does!).

*   **In the code:**
    ```python
    if __name__ == "__main__":
        # All the code indented below here runs at the start.
    ```

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
    from number_guessing import make_guess
    ```
    *   **`from number_guessing import make_guess`**: This imports our single game logic function from `number_guessing.py`.
    *   **`import gradio as gr`**: This imports the `gradio` library, giving it the alias `gr`.

#### 2. Creating the Interface with Gradio
The `gr.Interface` is the main object that creates our web UI. We configure it by telling it what function to use and what the inputs and outputs should look like.

*   **In the code:**
    ```python
    gr.Interface(
        fn=make_guess,
        inputs=gr.Number(label="Enter your guess (0-9)"),
        outputs="text",
        title="Simple Number Guessing Game"
    ).launch()
    ```
    *   **`fn=make_guess`**: Tells Gradio to call our `make_guess` function directly when the user submits a guess. All the game logic and state management happens within `make_guess`.
    *   **`inputs=gr.Number(...)`**: Defines the input field for the user's guess.
    *   **`outputs="text"`**: Defines the output field where feedback is displayed.
    *   **`.launch()`**: This starts the local web server and makes your game UI available in your browser.