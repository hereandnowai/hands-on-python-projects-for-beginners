# Project-Based Python: A Beginner's Guide to Building a Dice Rolling Simulator

**Welcome!** In this lesson, we will learn the fundamentals of Python programming by building a functional dice rolling simulator. We'll start with a simple command-line version and then create two different graphical user interfaces (UIs) for it. Every concept you learn will be something you immediately see and use in our project.

---

## Part 1: The Dice Rolling Logic (`die_rolling.py`)

This first file contains all the logic for our dice rolling simulator.

#### 1. Importing the `random` Module
To simulate rolling a die, we need to generate a random number. Python's built-in `random` module is perfect for this.

*   **In the code:**
    ```python
    import random
    ```

#### 2. Defining the `roll_die` Function
A function is a named, reusable block of code that performs a specific action. We use the `def` keyword to create one.

*   **In the code:**
    ```python
    def roll_die():
    ```
    *   **`def`**: The keyword that starts a function definition.
    *   **`roll_die`**: The name we have given our function.
    *   **`()`**: Since our function doesn't need any input to do its job, the parentheses are empty.

#### 3. Generating a Random Integer with `random.randint()`
This function from the `random` module returns a random integer within a specified range (inclusive).

*   **In the code:**
    ```python
    die_number = random.randint(1, 6)
    ```
    *   This will generate a random number between 1 and 6, just like a real die.

#### 4. The `return` Statement: Sending Back a Result
A function can send a value back to whoever called it using the `return` keyword.

*   **In the code:**
    ```python
    return die_number
    ```
    *   Our function sends the randomly generated number back as the result.

#### 5. The Main Execution Block: `if __name__ == "__main__":`
This is a special, standard Python construct. The code inside this block only runs when you execute the file directly from the terminal. It won't run if this file is imported into another file (like our UI files do!).

*   **In the code:**
    ```python
    if __name__ == "__main__":
        # All the code indented below here runs at the start.
    ```

#### 6. Loops and User Input
We use a `while True:` loop to keep the program running until the user decides to quit. The `input()` function prompts the user for input, and we use an `if/elif/else` block to handle their choice.

---

## Part 2: The User Interfaces (`simple_ui.py` and `better_ui.py`)

Now we'll take our dice rolling logic and give it a user-friendly graphical interface that can be opened in a web browser using the Gradio library.

### `simple_ui.py` - A Basic Interface

This file creates a very simple UI with a button to roll the die and an image to display the result.

#### 1. Importing and Defining the UI with `gr.Blocks`
*   **`import gradio as gr`**: Imports the Gradio library.
*   **`from die_rolling import roll_die`**: Imports our dice rolling function.
*   **`with gr.Blocks() as demo:`**: This creates a Gradio UI. We can add components to it inside this block.
*   **`gr.Markdown(...)`**, **`gr.Button(...)`**, **`gr.Image(...)`**: These are Gradio components that create the text, button, and image display area in our UI.

#### 2. Handling Button Clicks with `.click()`
*   **`roll_btn.click(...)`**: This tells Gradio what to do when the `roll_btn` is clicked.
    *   **`fn=roll_and_show_image`**: The function to call when the button is clicked.
    *   **`outputs=output_image`**: The component to send the function's return value to.

### `better_ui.py` - An Enhanced Interface

This file creates a more polished UI with branding, custom fonts, and a better layout.

#### 1. Reading Branding Information from `branding.json`
This UI reads information like the logo URL and slogan from the `branding.json` file, just like in the calculator project.

#### 2. Customizing the Theme with `gr.themes`
*   **`theme = gr.themes.Soft(...)`**: We create a theme object to customize the colors and fonts.
*   **`font=gr.themes.GoogleFont("Chau Philomene One")`**: This is the proper way to apply a custom font from Google Fonts to your Gradio application.

#### 3. Launching the App
*   **`demo.launch(...)`**: This starts the web server for the Gradio UI.
*   **`favicon_path=brand_data["logo"]["favicon"]`**: This sets the icon that appears in the browser tab.