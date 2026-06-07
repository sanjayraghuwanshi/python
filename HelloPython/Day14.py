"""
Day 14 — Week 2 Mini Project: Contact Book
Project: Build a contact book using a dictionary where each contact is stored
with name as the key and their details as a nested dictionary.

Features:
Add a new contact (name, phone, email, city).
Search for a contact by name (case-insensitive).
Update a contact's phone or email.
Delete a contact.
Display all contacts sorted alphabetically.
Show all contacts from a given city.
Run it as a menu-driven console app:

1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Filter by City
7. Exit
"""
sample = {
    "Arjun Mehta": {
        "phone": "+91-98765-43210",
        "email": "arjun.m@example.com",
        "city": "Mumbai"
    },
    "Raju Rao": {
        "phone": "+91-77665-54433",
        "email": "Raju.rao@hr.com",
        "city": "Hyderabad"
    }
}

import os

contacts = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact")
        print("5. View All Contacts\n6. Filter by City\n7. Exit")

        choice = input("\nEnter choice (1-7): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            city = input("Enter City: ")
            contacts[name] = {"phone": phone, "email": email, "city": city}
            print(f"Contact {name} added successfully!")

        elif choice == '2':
            search_name = input("Enter name to search: ").lower()
            # Case-insensitive search using a loop
            found = False
            for name, details in contacts.items():
                if search_name in name.lower():
                    print(
                        f"\nFound: {name} | Phone: {details['phone']} | Email: {details['email']} | City: {details['city']}")
                    found = True
                    break
            if not found: print("Contact not found.")

        elif choice == '3':
            name = input("Enter name to update: ")
            if name in contacts:
                print("1. Update Phone\n2. Update Email")
                up_choice = input("Select option: ")
                if up_choice == '1':
                    contacts[name]['phone'] = input("Enter new phone: ")
                elif up_choice == '2':
                    contacts[name]['email'] = input("Enter new email: ")
                print("Updated!")
            else:
                print("Contact not found.")

        elif choice == '4':
            name = input("Enter name to delete: ")
            if contacts.pop(name, None):
                print(f"{name} deleted.")
            else:
                print("Contact not found.")

        elif choice == '5':
            print("\n--- ALL CONTACTS (Sorted) ---")
            for name in sorted(contacts.keys()):
                d = contacts[name]
                print(f"{name.ljust(15)} | {d['phone'].ljust(12)} | {d['city']}")

        elif choice == '6':
            filter_city = input("Enter City: ").lower()
            print(f"\n--- Contacts in {filter_city.title()} ---")
            for name, details in contacts.items():
                if details['city'].lower() == filter_city:
                    print(f"{name} ({details['phone']})")

        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()
