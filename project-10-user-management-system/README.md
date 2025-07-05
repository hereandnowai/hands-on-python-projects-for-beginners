# Project-Based Python: A Beginner's Guide to Building a User Management System

**Welcome!** In this lesson, we will learn the fundamentals of Python programming by building a simple user management system. This system will allow you to add, update, delete, search, and display user entries. We'll create both a command-line version and a web-based user interface for it.

---

## Part 1: The System's Brain (`user_management_system.py`)

This file contains all the core logic for our user management system.

#### 1. Global Database
Our system uses a simple Python dictionary (`database`) to store entries. Each entry is itself a dictionary with fields like `srno`, `name`, `age`, `gender`, and `occupation`.

*   **In the code:**
    ```python
    database = {'entries': []}
    ```

#### 2. Defining Constants
We use constants for the field names to avoid typos and make the code more readable.

*   **In the code:**
    ```python
    SRNO = 'srno'
    NAME = 'name'
    # ... and so on
    ```

#### 3. Core Management Functions
Each function performs a specific operation on the `database`.

*   **`get_serial_no()`**: Generates a unique serial number for new entries.

*   **`add_entry(name, age, gender, occupation)`**: Adds a new user entry to the database.

*   **`find_entry_index(search_by, search_value)`**: A helper function that searches for an entry based on a given field and value, returning its index in the `entries` list or -1 if not found.

*   **`search_entry(search_by, search_value)`**: Uses `find_entry_index` to locate an entry and returns the entry dictionary if found, otherwise `None`.

*   **`update_entry(search_by, search_value, new_name, new_age, new_gender, new_occupation)`**: Finds an existing entry and updates its details.

*   **`delete_entry(search_by, search_value)`**: Finds and removes an entry from the database.

*   **`get_all_entries_display()`**: Returns a formatted string containing all entries in the database, suitable for display.

*   **`reset_database()`**: Clears all entries from the database.

#### 4. The Main Execution Block: `if __name__ == "__main__":`
This special block contains the command-line interface for the user management system. It runs only when `user_management_system.py` is executed directly.

---

## Part 2: The User Interface (`user_management_system_ui.py`)

This file provides a user-friendly graphical interface for the user management system using Gradio.

#### 1. Importing Necessary Modules
*   **`import gradio as gr`**: Imports the Gradio library for building the UI.
*   **`import json`, `import os`**: Used for handling branding data and file paths.
*   **`from user_management_system import ...`**: Imports all the necessary management functions and constants from `user_management_system.py`.

#### 2. Branding and Theming
The UI integrates branding elements (logo, slogan, colors, social media links) from your `branding.json` file and uses a custom Google Font (`Chau Philomene One`) for a consistent and polished look.

#### 3. Gradio Interface Structure
The UI is built using `gr.Blocks` for a more flexible layout. It organizes different operations (Add, Update, Delete, Search, Display All, Reset) into separate tabs, making the interface clean and intuitive.

*   **Input Components**: Uses `gr.Textbox`, `gr.Number`, and `gr.Radio` for user input.
*   **Output Components**: Uses `gr.Textbox` to display status messages and search results.
*   **Buttons**: Each operation has a dedicated button to trigger the corresponding function.

#### 4. Event Handling
Each button's `click` event is linked to the appropriate function imported from `user_management_system.py`, passing the UI inputs and updating the UI outputs.

---

## How to Run

To run this user management system, you first need to install the `gradio` library. If you haven't already, you can install it via `pip`:

```bash
pip install gradio
```

### Command-Line Interface

To run the command-line version, execute `user_management_system.py`:

```bash
python user_management_system.py
```

### Graphical User Interface

To run the Gradio UI, execute `user_management_system_ui.py`:

```bash
python user_management_system_ui.py
```

This will launch a web server with the user interface. You can access it by opening the provided URL in your web browser.