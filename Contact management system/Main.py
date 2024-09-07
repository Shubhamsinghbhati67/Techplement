import os
import json
import re

CONTACT_FILE = 'contacts.json'

def load_contacts():
    try:
        if not os.path.exists(CONTACT_FILE):
            return {}
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Could not decode the contacts file. It might be corrupted.")
        return {}
    except Exception as e:
        print(f"Error: Failed to load contacts. Details: {e}")
        return {}

def save_contacts(contacts):
    """Saving contacts to a JSON file."""
    try:
        with open(CONTACT_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
    except Exception as e:
        print(f"Error: Failed to save contacts. Details: {e}")

def is_valid_phone(phone):
    """Validate phone number """
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
    """Validate email address """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def add_contact(contacts):
    """Add a new contact with validation."""
    name = input("Enter contact name: ").strip()
    if not name:
        print("Error: Contact name cannot be empty!")
        return
    if name in contacts:
        print("Error: Contact with this name already exists!")
        return

    phone = input("Enter contact phone number (10 digits): ").strip()
    if not is_valid_phone(phone):
        print("Error: Phone number must be exactly 10 digits and contain only digits!")
        return

    email = input("Enter contact email: ").strip()
    if not is_valid_email(email):
        print("Error: Invalid email address!")
        return

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the name of the contact to search: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return

    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Error: No contact found with the name '{name}'.")

def update_contact(contacts):
    """Update an existing contact's information with validation."""
    name = input("Enter the name of the contact to update: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return

    if name in contacts:
        phone = input(
            f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        if phone and not is_valid_phone(phone):
            print("Error: Phone number must be exactly 10 digits and contain only digits!")
            return

        email = input(
            f"Enter new email (current: {contacts[name]['email']}): ").strip()
        if email and not is_valid_email(email):
            print("Error: Invalid email address!")
            return

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Error: No contact found with the name '{name}'.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Error: No contact found with the name '{name}'.")

def main():
    """Main function to run the contact management system."""
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Management System")
            break
        else:
            print("Error: Invalid choice. Please try again")

if __name__ == '__main__':
    main()
