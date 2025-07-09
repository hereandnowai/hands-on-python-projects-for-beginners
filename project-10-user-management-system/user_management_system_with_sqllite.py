from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import update, delete

# Constants (not used directly with SQLAlchemy but might be kept for the CLI)
SRNO = 'srno'
NAME = 'name'
AGE = 'age'
GENDER = 'gender'
OCCUPATION = 'occupation'


DB_NAME = 'user_database.db'  # Define database filename

# 1. Define the database engine (globally accessible)
engine = create_engine(f'sqlite:///./{DB_NAME}', echo=False)  # echo=True for debugging SQL
# 2. Define a base class for declarative models
Base = declarative_base()

# 3. Define a model for the 'users' table
class User(Base):
    __tablename__ = 'users'

    srno = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    occupation = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}, occupation='{self.occupation}')>"

# 4. Create the table (if it doesn't exist)
Base.metadata.create_all(engine)

# 5. Define Session class.  Create session as needed in functions.
Session = sessionmaker(bind=engine)


def get_serial_no(session):
    """Returns the next available serial number."""
    # Get the maximum srno value currently in the database
    max_srno = session.query(User).order_by(User.srno.desc()).first()
    if max_srno:
        return max_srno.srno + 1
    else:
        return 1 # Table is empty

def add_entry(name, age, gender, occupation):
    """Adds a new entry to the database using SQLAlchemy."""
    session = Session()  # Create a new session
    try:
        srno = get_serial_no(session)  # Get the next serial number
        new_user = User(srno=srno, name=name, age=age, gender=gender, occupation=occupation) # Use srno
        session.add(new_user)
        session.commit()
        return "Entry successfully created and saved to database."
    except Exception as e:
        session.rollback()  # Rollback in case of errors
        print(f"Error adding entry to database: {e}")
        return f"Error creating entry: {e}"
    finally:
        session.close()

def find_entry_index(search_by, search_value):
    """Finds the index of an entry based on database query rather than dictionary."""
    session = Session()
    try:
        # Convert the search value to lowercase for case-insensitive comparison.
        search_value_lower = str(search_value).lower()

        # Build the query based on the search_by field.
        if search_by == SRNO:
            query = session.query(User).filter(User.srno == int(search_value))
        elif search_by == NAME:
            query = session.query(User).filter(func.lower(User.name) == search_value_lower)
        elif search_by == AGE:
            query = session.query(User).filter(User.age == int(search_value))
        elif search_by == GENDER:
            query = session.query(User).filter(func.lower(User.gender) == search_value_lower)
        elif search_by == OCCUPATION:
            query = session.query(User).filter(func.lower(User.occupation) == search_value_lower)
        else:
            print(f"Invalid search_by field: {search_by}")
            return None  # Indicate that the search failed

        result = query.first()  # Fetch the first matching result (if any)

        if result:
            # Return the SRNO (primary key) of the found entry as the index/identifier.
            return result.srno
        else:
            # No matching entry found.
            return None  # Returning None if the entry is not found
    except Exception as e:
        print(f"Error during database query: {e}")
        return None  # Error during query

    finally:
        session.close()

def search_entry(search_by, search_value):
    """Searches for an entry in the database using SQLAlchemy."""
    session = Session()
    try:
        # Use the find_entry_index function to find the SRNO
        srno = find_entry_index(search_by, search_value)

        if srno:
            # Query the database to retrieve the entry by SRNO
            entry = session.query(User).filter_by(srno=srno).first()
            return entry  # Returns the User object if found
        else:
            # Entry not found
            return None
    except Exception as e:
        print(f"Error during database search: {e}")
        return None  # Error during the search
    finally:
        session.close()

def update_entry(search_by, search_value, new_name, new_age, new_gender, new_occupation):
    """Updates an entry in the database using SQLAlchemy."""
    session = Session()
    try:
        # find the entry SRNO to update with find_entry_index()
        srno = find_entry_index(search_by, search_value)

        if srno:
            # Use SQLAlchemy's update() function to update the entry
            session.query(User).filter(User.srno == srno).update({
                User.name: new_name,
                User.age: new_age,
                User.gender: new_gender,
                User.occupation: new_occupation
            })
            session.commit()
            return "Entry successfully updated in the database."
        else:
            return "Entry not found."
    except Exception as e:
        session.rollback()
        print(f"Error updating entry in database: {e}")
        return f"Error updating entry: {e}"
    finally:
        session.close()

def delete_entry(search_by, search_value):
    """Deletes an entry from the database using SQLAlchemy."""
    session = Session()
    try:
        # Find the entry SRNO to delete with find_entry_index()
        srno = find_entry_index(search_by, search_value)

        if srno:
            # Use SQLAlchemy's delete() function to delete the entry
            session.query(User).filter(User.srno == srno).delete()
            session.commit()
            return "Entry successfully deleted from the database."
        else:
            return "Entry not found."
    except Exception as e:
        session.rollback()
        print(f"Error deleting entry from database: {e}")
        return f"Error deleting entry: {e}"
    finally:
        session.close()

def get_all_entries_display():
    """Formats all entries for display (now using SQLAlchemy)."""
    session = Session()
    try:
        users = session.query(User).all()
        if not users:
            return "No entries to display."

        display_str = ""
        for user in users:
            display_str += f"SRNO: {user.srno}\n"
            display_str += f"Name: {user.name}\n"
            display_str += f"Age: {user.age}\n"
            display_str += f"Gender: {user.gender}\n"
            display_str += f"Occupation: {user.occupation}\n\n"
        return display_str.strip()
    except Exception as e:
        print(f"Error retrieving entries: {e}")
        return "Error retrieving entries."
    finally:
        session.close()

def reset_database():
    """Resets the database (both dictionary and SQLite)."""
    session = Session()
    try:
        # Delete all entries from the User table
        session.query(User).delete()
        session.commit()
        return "Database reset (all entries deleted)."
    except Exception as e:
        session.rollback()
        print(f"Error resetting database: {e}")
        return f"Error resetting database: {e}"
    finally:
        session.close()

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
        print("6. Reset Database")
        print("7. Exit")
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
                    print(f"SRNO: {entry.srno}")
                    print(f"Name: {entry.name}")
                    print(f"Age: {entry.age}")
                    print(f"Gender: {entry.gender}")
                    print(f"Occupation: {entry.occupation}\n")
                else:
                    print("Entry not found.\n")
            elif choice == 5:
                print("\nAll Entries:\n")
                print(get_all_entries_display())
            elif choice == 6:
                print(reset_database())
            elif choice == 7:
                print('Exiting')
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")