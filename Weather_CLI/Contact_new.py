contacts = []

def add_contact(name, phone):
    contacts.append({"Name": name, "Phone": phone})
    print("Contact added.")

def search_contact(name):
    found = False
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            found = True
    if not found:
        print("Contact not found.")

def list_contacts():
    if not contacts:
        print("No contacts in the list.")
    else:
        for contact in contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")

while True:
    print("\nContact List Application")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. List Contacts")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        list_contacts()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
