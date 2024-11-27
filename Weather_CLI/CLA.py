import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def edit_contact(self, index, name, phone, email):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.name = name
            contact.phone = phone
            contact.email = email
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Deleted contact: {deleted_contact.name}")
        else:
            print("Invalid contact index.")

    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            contacts_data = [{'name': contact.name, 'phone': contact.phone, 'email': contact.email} for contact in self.contacts]
            json.dump(contacts_data, file)

    def load_contacts(self, filename):
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(contact['name'], contact['phone'], contact['email']) for contact in contacts_data]
        except FileNotFoundError:
            print("Contact file not found. Starting with an empty contact list.")

def main():
    contact_list = ContactList()
    contact_list.load_contacts("contacts.json")

    while True:
        print("\nContact List Application")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save and Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            contact_list.view_contacts()
        elif choice == "2":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact_list.add_contact(name, phone, email)
        elif choice == "3":
            index = int(input("Enter the index of the contact to edit: "))
            name = input("Enter New Name: ")
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            contact_list.edit_contact(index, name, phone, email)
        elif choice == "4":
            index = int(input("Enter the index of the contact to delete: "))
            contact_list.delete_contact(index)
        elif choice == "5":
            contact_list.save_contacts("contacts.json")
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()
