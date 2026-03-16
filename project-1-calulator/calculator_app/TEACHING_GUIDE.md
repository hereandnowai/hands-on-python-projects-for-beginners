# Teaching Guide: Building a Flask Calculator App

Welcome! This guide will take you through the process of building the iPhone-style Calculator App from scratch. We will move from core logic to a fully functional web application.

## Table of Contents
1. [Prerequisites & Environment Setup](#1-prerequisites--environment-setup)
2. [Step 1: Core Logic (The Brain)](#step-1-core-logic-the-brain)
3. [Step 2: The Web Server (The Skeleton)](#step-2-the-web-server-the-skeleton)
4. [Step 3: The User Interface (The Body)](#step-3-the-user-interface-the-body)
5. [Step 4: Putting it All Together](#step-4-putting-it-all-together)
6. [How to Run the Project](#how-to-run-the-project)

---

## 1. Prerequisites & Environment Setup

Before we start, ensure you have Python installed on your machine.

### Create a Virtual Environment
It's a best practice to keep your project dependencies isolated.
```bash
# Navigate to your project folder
cd project-1-calculator/calculator_app

# Create a virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Install Dependencies
This project uses **Flask**, a lightweight web framework for Python.
```bash
pip install -r requirements.txt
```

---

## Step 1: Core Logic (The Brain)

We start by writing the mathematical logic. This is independent of the web interface.

**File:** [backend/calculator_logic.py](backend/calculator_logic.py)

- Create a function `calculate(a, op, b)`.
- Use `if/elif` statements to handle `+`, `-`, `*`, and `/`.
- **Edge Case:** Remember to handle division by zero!

---

## Step 2: The Web Server (The Skeleton)

Now we use Flask to create a bridge between the user and our Python logic.

**File:** [app.py](app.py)

1. **Initialize Flask:** `app = Flask(__name__)`
2. **Define Routes:**
   - `/`: Serves the HTML page.
   - `/calculate`: A `POST` route that receives numbers from the frontend, calls `calculate()`, and returns the result as JSON.
3. **App Run:** Use `app.run(debug=True)` so the server restarts automatically when you make changes.

---

## Step 3: The User Interface (The Body)

A web app needs a face. We use HTML for structure, CSS for the "iPhone look," and JavaScript for interactivity.

### HTML Structure
**File:** [templates/index.html](templates/index.html)
- Define a `display` input.
- Create buttons for numbers (0-9) and operators (+, -, *, /).

### Styling (CSS)
**File:** [static/css/styles.css](static/css/styles.css)
- Use Flexbox or Grid to align buttons.
- Create the signature rounded buttons and dark theme.

### Interactivity (JavaScript)
**File:** [static/js/script.js](static/js/script.js)
- Maintain a local state for the current input.
- When the `=` button is pressed, use `fetch()` to send the data to our `/calculate` endpoint in [app.py](app.py).

---

## Step 4: Putting it All Together

1. The user clicks buttons in the browser ([index.html](templates/index.html)).
2. JavaScript ([script.js](static/js/script.js)) collects the numbers and sends them to the server.
3. Flask ([app.py](app.py)) receives the request and calls the Python function ([calculator_logic.py](backend/calculator_logic.py)).
4. The result is sent back to the browser and updated on the display.

---

## How to Run the Project

Once everything is set up:
1. Ensure your virtual environment is active.
2. Run the server:
   ```bash
   python app.py
   ```
3. Open your browser and go to: `http://127.0.0.1:5000`

Happy Coding!
