# Project-Based Python: A Beginner's Guide to Building a Countdown Timer

**Welcome!** In this lesson, we will learn the fundamentals of Python programming by building a functional countdown timer. We'll start with a simple command-line version and then create a web-based user interface for it. Every concept you learn will be something you immediately see and use in our project.

---

## Part 1: The Timer's Brain (`countdown_timer.py`)

This first file contains all the core logic for our countdown timer.

#### 1. Importing the `time` Module
To make our timer actually count down, we need to pause the program for a short duration. Python's built-in `time` module provides functions for this.

*   **In the code:**
    ```python
    import time
    ```

#### 2. The `set_countdown()` Function: The Core Logic
This function handles the actual countdown process. It's designed to work both with the command-line interface and the Gradio UI.

*   **In the code:**
    ```python
    def set_countdown(seconds):
        yield "Countdown starts now..."
        for i in range(seconds, 0, -1):
            yield f'{i:02d}'
            time.sleep(1)
        yield "Countdown ended!"
    ```
    *   **`yield` Keyword**: This is a special Python keyword that turns a function into a **generator**. Instead of returning a single value and ending, a generator can `yield` multiple values over time. This is perfect for Gradio's streaming output, allowing the UI to update in real-time as the countdown progresses.
    *   **`for i in range(seconds, 0, -1)`**: This loop counts down from the `seconds` provided, down to 1.
    *   **`time.sleep(1)`**: Pauses the program for 1 second, creating the countdown effect.
    *   **`f'{i:02d}'`**: Formats the number `i` to always have at least two digits (e.g., `5` becomes `05`), which looks nicer in a countdown.

#### 3. The Main Execution Block: `if __name__ == "__main__":`
This is a special, standard Python construct. The code inside this block only runs when you execute the file directly from the terminal. It won't run if this file is imported into another file (like our UI file does!).

*   **In the code:**
    ```python
    if __name__ == "__main__":
        # All the code indented below here runs at the start.
    ```

#### 4. User Interaction: `print()`, `input()`, and Data Types
*   **`print()`**: Displays text or variables to the user in the console.
*   **`input()`**: Pauses the program, prompts the user with a message, and waits for them to type something and press Enter. It always returns the input as a string (text).
*   **Type Casting with `int()`**: Since `input()` gives us text, we must convert it to an integer (`int()`) before we can use it as the number of seconds.

---

## Part 2: The User Interface (`countdown_timer_ui.py`)

Now we'll take our timer logic and give it a user-friendly graphical interface that can be opened in a web browser.

#### 1. Importing: Using Code from Other Files and Libraries
Importing allows us to use functions and tools from other files or from external packages that other developers have built.

*   **In the code:**
    ```python
    import gradio as gr
    from countdown_timer import set_countdown
    import json
    import os
    ```
    *   **`from countdown_timer import set_countdown`**: This imports our timer function from `countdown_timer.py`.
    *   **`import gradio as gr`**: This imports the `gradio` library, giving it the alias `gr`.
    *   **`import json`, `import os`**: Used for handling branding data and file paths.

#### 2. Branding Integration
The UI integrates branding elements (logo, slogan, colors, social media links) from your `branding.json` file, ensuring a consistent look and feel.

#### 3. Creating the Interface with Gradio
The `gr.Blocks` object is used to create a more complex UI layout. We configure it by telling it what function to use and what the inputs and outputs should look like.

*   **In the code:**
    ```python
    with gr.Blocks(theme=theme) as demo:
        # ... UI components like Image, Markdown, Number input, Button, Textbox ...
        start_button.click(fn=set_countdown, inputs=seconds_input, outputs=output_text)
    ```
    *   **`fn=set_countdown`**: Tells Gradio to call our `set_countdown` function when the `start_button` is clicked. Because `set_countdown` is a generator (uses `yield`), Gradio automatically handles the streaming updates to the `output_text` box.
    *   **`inputs=seconds_input`**: Defines the input field for the number of seconds.
    *   **`outputs=output_text`**: Defines the output field where the countdown status is displayed.
    *   **`.launch()`**: This starts the local web server and makes your timer UI available in your browser.

---

## How to Run

To run this countdown timer, you first need to install the `gradio` library if you plan to use the UI. If you haven't already, you can install it via `pip`:

```bash
pip install gradio
```

### Command-Line Interface

To run the command-line version, execute `countdown_timer.py`:

```bash
python countdown_timer.py
```

### Graphical User Interface

To run the Gradio UI, execute `countdown_timer_ui.py`:

```bash
python countdown_timer_ui.py
```

This will launch a web server with the user interface. You can access it by opening the provided URL in your web browser.