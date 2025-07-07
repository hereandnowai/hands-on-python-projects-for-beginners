# --- Database ---
# A dictionary acting as a simple in-memory database.
# The 'entries' key holds a list of user records (which are also dictionaries).
database = {'entries': []}

# --- Constants for Dictionary Keys ---
# Using constants helps prevent typos when accessing dictionary fields.
SRNO = 'srno'
NAME = 'name'
AGE = 'age'
GENDER = 'gender'
OCCUPATION = 'occupation'

def get_serial_no():
    # 1. The serial number should be one more than the current number of entries.
    #    Calculate this based on the length of the `database['entries']` list.
    # 2. Return the calculated serial number.
    pass # Remove this line and add your code here

def add_entry(name, age, gender, occupation):
    # 3. Create a new dictionary called `entry`.
    # 4. Populate the `entry` dictionary with the provided arguments.
    #    - Use the constants (SRNO, NAME, etc.) as keys.
    #    - Call `get_serial_no()` to get the 'srno'.
    # 5. Append the new `entry` dictionary to the `database['entries']` list.
    # 6. Return a success message, e.g., "Entry successfully created."
    pass # Remove this line and add your code here

def find_entry_index(search_by, search_value):
    # 7. Loop through the `database['entries']` list with an index (use `enumerate`).
    # 8. In each iteration, get the `entry` dictionary.
    # 9. Check if the value of the `search_by` key in the `entry` matches the `search_value`.
    #    - Convert both to strings and lowercase for a case-insensitive search.
    # 10. If a match is found, return the index `i`.
    # 11. If the loop finishes without a match, return -1.
    pass # Remove this line and add your code here

def search_entry(search_by, search_value):
    # 12. Call `find_entry_index()` to get the index of the entry.
    # 13. If the index is not -1, return the entry from the database list.
    # 14. Otherwise, return `None`.
    pass # Remove this line and add your code here

def update_entry(search_by, search_value, new_name, new_age, new_gender, new_occupation):
    # 15. Find the index of the entry to update using `find_entry_index()`.
    # 16. If the index is not -1:
    #     a. Access the entry dictionary at that index.
    #     b. Update its values (name, age, etc.) with the new data.
    #     c. Return a success message.
    # 17. If the index is -1, return an "Entry not found" message.
    pass # Remove this line and add your code here

def delete_entry(search_by, search_value):
    # 18. Find the index of the entry to delete.
    # 19. If the index is not -1:
    #     a. Use `del database['entries'][index]` to remove the entry.
    #     b. Return a success message.
    # 20. If the index is -1, return an "Entry not found" message.
    pass # Remove this line and add your code here

def get_all_entries_display():
    # 21. Check if the database is empty. If so, return "No entries to display."
    # 22. Create a formatted string that lists all details for all entries.
    #     - Loop through each entry in the database.
    #     - For each entry, append its details (SRNO, Name, Age, etc.) to the string.
    # 23. Return the complete, formatted string.
    pass # Remove this line and add your code here

def reset_database():
    # 24. Use the `global` keyword to modify the `database` variable.
    # 25. Reset the database to its initial empty state: `{'entries': []}`.
    # 26. Return a confirmation message.
    pass # Remove this line and add your code here

if __name__ == "__main__":
    # 27. Implement the command-line interface (CLI).
    #     - Print a welcome message.
    #     - Start a `while True` loop for the main menu.
    #     - Display options: Add, Update, Delete, Search, Display All, Exit.
    #     - Get the user's choice.
    #     - Use an if-elif-else structure to call the appropriate functions based on the choice.
    #     - For operations like update and delete, you'll need to ask the user how they want to find the entry (e.g., by name, by srno).
    #     - Use `try-except` blocks to handle invalid integer inputs for menu choices.
    pass # Remove this line and implement the CLI.
