# Things to learn before beginning the project:
## Part 1:
- Python function: what, why, how
- Function: colon, arguments/ parameters
- return
- Conditionals - if, elif, else - ends with a colon
- indentation
- Operators - math function
- Print statement
- Loop: for, while
- Variable (how to name a variable - it cannot start with a number, space, no special characters, no default functions,)
- Input function - how to take input from a user
- Break & continue
- Float, int, string
- What is f string
## Part 2:      
- Import function
- Path, Gradio & use cases.

# Project-Based Python: A Beginner's Guide to Building a Calculator

**Welcome!** In this lesson, we will learn the fundamentals of Python programming by building a functional calculator. We'll start with a simple command-line version and then create a beautiful web-based user interface for it. Every concept you learn will be something you immediately see and use in our project.

---

## Part 1: The Calculator's Brain (`calculator.py`)

This first file contains all the logic for performing our calculations.

#### 1. Defining Functions: Creating Reusable Code
A function is a named, reusable block of code that performs a specific action. We use the `def` keyword to create one.

*   **In the code:**
    ```python
    def calculate(num1, op, num2):
    ```
    *   **`def`**: The keyword that starts a function definition.
    *   **`calculate`**: The name we have given our function.
    *   **`(num1, op, num2)`**: These are **parameters**, which are placeholders for the data (arguments) the function will need to work. Our `calculate` function needs a first number, an operator, and a second number.

#### 2. Conditional Logic: Making Decisions with `if` and `elif`
Conditional statements allow a program to execute different code blocks depending on whether a condition is `True` or `False`.

*   **In the code:**
    ```python
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        # ...
    ```
    *   **`if op == "+":`**: This checks if the `op` variable is equal to the string `"+"`. The `==` is a comparison operator.
    *   **`elif`**: Short for "else if," this checks a new condition if the previous `if` (or `elif`) was `False`.
    *   **Nested Conditions**: You can put `if` statements inside other `if` statements for more complex logic. We do this to handle division by zero.
        ```python
        if num2 == 0:
            return "Error: Division by zero"
        ```

#### 3. The `return` Statement: Sending Back a Result
A function can send a value back to whoever called it using the `return` keyword.

*   **In the code:**
    ```python
    return num1 + num2
    ```
    *   When the operator is `+`, our function calculates the sum and sends the result back.

#### 4. The Main Execution Block: `if __name__ == "__main__":`
This is a special, standard Python construct. The code inside this block only runs when you execute the file directly from the terminal. It won't run if this file is imported into another file (like our UI file does!).

*   **In the code:**
    ```python
    if __name__ == "__main__":
        # All the code indented below here runs at the start.
    ```

#### 5. Loops: Repeating Actions with `while`
A `while` loop will repeat the code inside it as long as its condition is `True`.

*   **In the code:**
    ```python
    while True:
        # ... code to ask for input and calculate ...
    ```
    *   **`while True:`**: This creates an infinite loop. We need a way to get out!
    *   **`break`**: The `break` keyword immediately exits the current loop. We use it to stop the program when the user types 'exit'.
        ```python
        if choice == 'exit':
            break
        ```
    *   **`continue`**: The `continue` keyword skips the rest of the current loop iteration and jumps back to the top. We use it to ask for input again if the user enters an invalid operator.
        ```python
        if choice not in "+-*/":
            print("Invalid choice.")
            continue
        ```

#### 6. User Interaction: `print()`, `input()`, and Data Types
*   **`print()`**: Displays text or variables to the user in the console.
    ```python
    print("===== Welcome to The HERE AND NOW Calculator App =====\n")
    ```
*   **`input()`**: Pauses the program, prompts the user with a message, and waits for them to type something and press Enter. It always returns the input as a string (text).
    ```python
    choice = input("Enter an operator: ")
    ```
*   **Type Casting with `float()`**: Since `input()` gives us text, we must convert it to a number before we can do math. `float()` converts a string into a floating-point number (a number that can have decimals).
    ```python
    num1 = float(input("Enter first number: "))
    ```
*   **f-strings**: A modern and easy way to include variables directly inside a string.
    ```python
    result = calculate(num1, choice, num2)
    print(f"Output: {result}")
    ```

---

## Part 2: The User Interface (`cal_ui.py`)

Now we'll take our calculator logic and give it a user-friendly graphical interface that can be opened in a web browser.

#### 1. Importing: Using Code from Other Files and Libraries
Importing allows us to use functions and tools from other files or from external packages that other developers have built.

*   **In the code:**
    ```python
    from calculator import calculate
    import gradio as gr
    import json
    import os
    ```
    *   **`from calculator import calculate`**: This imports *only* the `calculate` function from our `calculator.py` file.
    *   **`import gradio as gr`**: This imports an external library named `gradio` and gives it a shorter alias, `gr`, for convenience.
    *   **`import json`**: This imports Python's built-in library for working with JSON data.
    *   **`import os`**: This imports the `os` module, which helps us interact with the operating system, especially for handling file paths.

#### 2. External Libraries: `gradio` and `pip`
`gradio` is an external library that makes it very easy to create web UIs for Python scripts. To use it, we first need to install it using Python's package installer, **`pip`**. You would run this command in your terminal:
```bash
pip install gradio
```

#### 3. Reading from Files: `open()`, `os`, and `json`
*   **File Paths with `os`**: To reliably find our `branding.json` file, we use the `os` module. This code builds an absolute path to the file, no matter where you run the script from.
    ```python
    branding_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'branding.json'))
    ```
*   **Opening Files with `with open()`**: This is the standard way to open a file. It ensures the file is automatically closed when you're done with it.
    ```python
    with open(branding_path) as f:
        # ... do something with the file f
    ```
*   **JSON**: JSON is a simple, text-based format for storing and exchanging data. Our `branding.json` file likely contains information like our app's name and slogan.
*   **Loading JSON Data**: The `json.load()` function reads a file containing JSON and converts it into a Python dictionary, which is a way of storing data in `key: value` pairs.
    ```python
    brand_data = json.load(f)["brand"]
    ```

#### 4. Creating the Interface with Gradio
The `gr.Interface` is the main object that creates our web UI. We configure it by telling it what function to use and what the inputs and outputs should look like.

*   **In the code:**
    ```python
    gr.Interface(
        fn=calculate,
        inputs=[gr.Number(label="First Number"), gr.Radio(["+", "-", "*", "/"], label="Operation"), gr.Number(label="Second Number")],
        outputs=gr.Textbox(label="Result"),
        title=brand_data["organizationShortName"],
        description=brand_data["slogan"],
        theme=gr.themes.Soft()
    ).launch()
    ```
    *   **`fn=calculate`**: Tells Gradio to call our `calculate` function when the user submits the form.
    *   **`inputs=[...]`**: Defines the input fields. `gr.Number` creates a box for numbers, and `gr.Radio` creates selectable radio buttons.
    *   **`outputs=gr.Textbox(...)`**: Defines the output field. `gr.Textbox` creates a text area to display the result.
    *   **`title` and `description`**: Sets the text that appears at the top of the web page, which we loaded from our JSON file.
    *   **`.launch()`**: This is the final command that starts the local web server and makes your calculator UI available in your browser.