# Project-Based Python: A Beginner's Guide to Building a Rock, Paper, Scissors Game

**Welcome!** In this lesson, we will learn the fundamentals of Python programming by building a classic Rock, Paper, Scissors game. We'll create both a command-line version and a web-based user interface for it. Every concept you learn will be something you immediately see and use in our project.

---

## Part 1: The Game's Brain (`rock_paper_scissor.py`)

This file contains all the core logic for our Rock, Paper, Scissors game.

#### 1. Importing the `random` Module
To make the computer's move unpredictable, we use Python's built-in `random` module.

*   **In the code:**
    ```python
    import random
    ```

#### 2. Defining Game Constants
We define constants for the moves (`ROCK`, `PAPER`, `SCISSOR`) and a list of all possible `choices`. We also define `winning_conditions` as a dictionary to easily determine the winner of a round.

*   **In the code:**
    ```python
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSOR = 'scissor'
    choices = [ROCK, PAPER, SCISSOR]
    winning_conditions = {
        ROCK: SCISSOR,
        PAPER: ROCK,
        SCISSOR: PAPER
    }
    ```

#### 3. Core Game Functions

*   **`get_computer_move()`**: Randomly selects one of the `choices` for the computer's move.

*   **`play_round(user_move_str)`**: This is the central function for playing a single round of the game.
    *   It takes the user's move as a string.
    *   It gets a random move for the computer.
    *   It compares the user's move and the computer's move using the `winning_conditions`.
    *   It returns a comprehensive message indicating both players' moves and the outcome of the round (Win, Lose, or Tie).

#### 4. The Main Execution Block: `if __name__ == "__main__":`
This special block contains the command-line interface for the game. It runs only when `rock_paper_scissor.py` is executed directly, allowing you to play the game in your terminal.

---

## Part 2: The User Interface (`rock_paper_scissor_ui.py`)

This file provides a user-friendly graphical interface for the Rock, Paper, Scissors game using Gradio.

#### 1. Importing Necessary Modules
*   **`import gradio as gr`**: Imports the Gradio library for building the UI.
*   **`import json`, `import os`**: Used for handling branding data and file paths.
*   **`from rock_paper_scissor import play_round`**: Imports the core game logic function from `rock_paper_scissor.py`.

#### 2. Branding and Theming
The UI integrates branding elements (logo, slogan, colors, social media links) from your `branding.json` file and uses a custom Google Font (`Chau Philomene One`) for a consistent and polished look.

#### 3. Gradio Interface Structure
The UI is built using `gr.Blocks` for a more flexible layout. It includes:
*   **Image**: Displays your brand logo.
*   **Markdown**: Shows your brand slogan and instructions.
*   **`gr.Radio`**: Allows the user to select their move (Rock, Paper, or Scissor).
*   **`gr.Button`**: To trigger the game round.
*   **`gr.Textbox`**: To display the game result.

#### 4. Event Handling
*   **`play_button.click(...)`**: Calls the `play_round` function when the play button is clicked, updating the game result display.

---

## How to Run

To run this Rock, Paper, Scissors game, you first need to install the `gradio` library. If you haven't already, you can install it via `pip`:

```bash
pip install gradio
```

### Command-Line Interface

To run the command-line version, execute `rock_paper_scissor.py`:

```bash
python rock_paper_scissor.py
```

### Graphical User Interface

To run the Gradio UI, execute `rock_paper_scissor_ui.py`:

```bash
python rock_paper_scissor_ui.py
```

This will launch a web server with the user interface. You can access it by opening the provided URL in your web browser.