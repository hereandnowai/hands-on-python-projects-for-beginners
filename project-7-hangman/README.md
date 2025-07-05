# Project-Based Python: A Beginner's Guide to Building a Hangman Game

**Welcome!** In this lesson, we will learn the fundamentals of Python programming by building a classic Hangman game. We'll create both a command-line version and a web-based user interface for it. Every concept you learn will be something you immediately see and use in our project.

---

## Part 1: The Game's Brain (`hangman.py`)

This file contains all the core logic for our Hangman game.

#### 1. Importing Necessary Modules
*   **`import random`**: Used to select a random word from our wordlist.
*   **`import os`**: Used to handle file paths, ensuring our wordlist is found correctly regardless of where the script is run from.

#### 2. Global Game State Variables
To manage the game's progress across different turns and functions, we use **global variables**. These variables store the current state of the game.

*   **`secret_word`**: The word the player needs to guess.
*   **`display_word`**: The word shown to the player, with unguessed letters replaced by underscores (e.g., `_ _ _ _`).
*   **`chances_remaining`**: The number of incorrect guesses the player has left.
*   **`guessed_letters`**: A set to keep track of all letters the player has already guessed.

#### 3. Core Game Functions

*   **`get_random_word_from_wordlist()`**: Reads words from `hangman_wordlist.txt` and selects one at random.
    *   **File Handling**: Demonstrates how to open and read from a text file.
    *   **Path Handling**: Uses `os.path.join(os.path.dirname(__file__), '..', 'hangman_wordlist.txt')` to build a reliable path to the wordlist, even if the script is run from a different directory.

*   **`get_hangman_drawing(chances)`**: Returns a string representation of the hangman figure based on the number of `chances` left.

*   **`initialize_game()`**: Sets up a new game by choosing a new `secret_word`, creating the initial `display_word` (all underscores), resetting `chances_remaining`, and clearing `guessed_letters`.

*   **`process_guess(character)`**: This is the central function for handling a player's guess.
    *   It checks if the guess is valid (single alphabet, not already guessed).
    *   If the guess is correct, it updates `display_word`.
    *   If the guess is incorrect, it reduces `chances_remaining`.
    *   It also checks if the game is won or lost and returns appropriate messages and updated game state.

#### 4. The Main Execution Block: `if __name__ == "__main__":`
This special block contains the command-line interface for the Hangman game. It runs only when `hangman.py` is executed directly, allowing you to play the game in your terminal.

---

## Part 2: The User Interface (`hangman_ui.py`)

This file provides a user-friendly graphical interface for the Hangman game using Gradio.

#### 1. Importing Necessary Modules
*   **`import gradio as gr`**: Imports the Gradio library for building the UI.
*   **`import json`, `import os`**: Used for handling branding data and file paths.
*   **`from hangman import initialize_game, process_guess, get_hangman_drawing`**: Imports the core game functions from `hangman.py`.

#### 2. Branding and Theming
The UI integrates branding elements (logo, slogan, colors, social media links) from your `branding.json` file and uses a custom Google Font (`Chau Philomene One`) for a consistent and polished look.

#### 3. Gradio Interface Structure
The UI is built using `gr.Blocks` for a more flexible layout. It includes:
*   **Image**: Displays your brand logo.
*   **Markdown**: Shows your brand slogan.
*   **`gr.Image`**: Displays the hangman drawing.
*   **`gr.Textbox`**: Shows the word to guess, chances left, and game status messages.
*   **`gr.Textbox` (input)**: For the user to enter their guess.
*   **`gr.Button`**: To submit a guess or start a new game.

#### 4. Event Handling
*   **`guess_button.click(...)`**: Calls the `make_a_guess` function (which in turn calls `process_guess` from `hangman.py`) when the guess button is clicked, updating the UI.
*   **`new_game_button.click(...)`**: Calls the `start_new_game` function (which calls `initialize_game` from `hangman.py`) to reset the game.
*   **`demo.load(...)`**: Automatically initializes a new game when the Gradio app loads in the browser.

---

## How to Run

To run this Hangman game, you first need to install the `gradio` library if you plan to use the UI. If you haven't already, you can install it via `pip`:

```bash
pip install gradio
```

### Command-Line Interface

To run the command-line version, execute `hangman.py`:

```bash
python hangman.py
```

### Graphical User Interface

To run the Gradio UI, execute `hangman_ui.py`:

```bash
python hangman_ui.py
```

This will launch a web server with the user interface. You can access it by opening the provided URL in your web browser.