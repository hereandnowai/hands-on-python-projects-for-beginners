database = {'entries': []}

SRNO = 'srno'
NAME = 'name'
AGE = 'age'
GENDER = 'gender'
OCCUPATION = 'occupation'

def get_serial_no():
    return len(database['entries']) + 1

def add_entry(name, age, gender, occupation):
    entry = {
        'srno': get_serial_no(),
        'name': name,
        'age': age,
        'gender': gender,
        'occupation': occupation
    }
    database['entries'].append(entry)
    return "Entry successfully created."

def find_entry_index(search_by, search_value):
    for i, entry in enumerate(database['entries']):
        if str(entry.get(search_by)).lower() == str(search_value).lower():
            return i
    return -1

def search_entry(search_by, search_value):
    index = find_entry_index(search_by, search_value)
    if index != -1:
        return database['entries'][index]
    return None

def update_entry(search_by, search_value, new_name, new_age, new_gender, new_occupation):
    index = find_entry_index(search_by, search_value)
    if index != -1:
        database['entries'][index][NAME] = new_name
        database['entries'][index][AGE] = new_age
        database['entries'][index][GENDER] = new_gender
        database['entries'][index][OCCUPATION] = new_occupation
        return "Entry successfully updated."
    return "Entry not found."

def delete_entry(search_by, search_value):
    index = find_entry_index(search_by, search_value)
    if index != -1:
        del database['entries'][index]
        return "Entry successfully deleted."
    return "Entry not found."

def get_all_entries_display():
    if not database['entries']:
        return "No entries to display."
    
    display_str = ""
    for entry in database['entries']:
        display_str += f"SRNO: {entry['srno']}\n"
        display_str += f"Name: {entry['name']}\n"
        display_str += f"Age: {entry['age']}\n"
        display_str += f"Gender: {entry['gender']}\n"
        display_str += f"Occupation: {entry['occupation']}\n\n"
    return display_str.strip()

def reset_database():
    global database
    database = {'entries': []}
    return "Database reset."

# --- Command-line Interface (for direct execution) ---
if __name__ == "__main__":
    def select_entry_and_value_cli():
        search_fields = {1: SRNO, 2: NAME, 3: AGE, 4: GENDER, 5: OCCUPATION}
        while True:
            print('Choose an entry based on which to search entries in database: ')
            for key, value in search_fields.items():
                print(f"{key}. {value}")
            try:
                choice = int(input("Enter your choice: "))
                if choice in search_fields:
                    value_type = search_fields[choice]
                    search_value = input(f"Enter {value_type} to search: ")
                    return value_type, search_value
                else:
                    print("Invalid input...please try again")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_entry_details_cli():
        name = input("Enter name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        occupation = input("Enter occupation: ")
        return name, age, gender, occupation

    print("===== Welcome To User Management System =====")
    while True:
        print("\nWhat would you like to do:-")
        print("1. Add an entry")
        print("2. Update an entry")
        print("3. Delete an entry")
        print("4. Search an entry")
        print("5. Display all entries")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Enter details for the new entry:-")
                name, age, gender, occupation = get_entry_details_cli()
                print(add_entry(name, age, gender, occupation))
            elif choice == 2:
                search_by, search_value = select_entry_and_value_cli()
                print('Enter the details of the updated entry:-')
                new_name, new_age, new_gender, new_occupation = get_entry_details_cli()
                print(update_entry(search_by, search_value, new_name, new_age, new_gender, new_occupation))
            elif choice == 3:
                search_by, search_value = select_entry_and_value_cli()
                print(delete_entry(search_by, search_value))
            elif choice == 4:
                search_by, search_value = select_entry_and_value_cli()
                entry = search_entry(search_by, search_value)
                if entry:
                    print("\nEntry Found:")
                    print(f"SRNO: {entry['srno']}")
                    print(f"Name: {entry['name']}")
                    print(f"Age: {entry['age']}")
                    print(f"Gender: {entry['gender']}")
                    print(f"Occupation: {entry['occupation']}\n")
                else:
                    print("Entry not found.\n")
            elif choice == 5:
                print("\nAll Entries:\n")
                print(get_all_entries_display())
            elif choice == 6:
                print('Exiting')
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")