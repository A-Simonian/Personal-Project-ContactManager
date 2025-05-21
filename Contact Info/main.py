import csv
import os
from contact import Contact
from fileIO import open_file, writeContacts
from db import initialize_database

def is_duplicate(contact, contacts):
    for existing in contacts:
        if contact.name == existing.name and contact.email == existing.email:
            return True
    return False

def get_contact(next_id):
    name = input("Enter name: ").strip()
    while True:
        email = input("Enter email: ").strip()
        if Contact.is_valid_email(email):
            break
        print("Invalid email. Try again")
    while True:
        phoneNumber = input("Enter phone number: ").strip()
        if Contact.is_valid_phone(phoneNumber):
            break
        print("Invalid phone number. Try again")

    contactID = next_id

    contact = Contact(contactID, name, email, phoneNumber)

    return contact, next_id + 1

def updateContact(contact):

    while True:
        print("Update:")
        print("1. Name")
        print("2. Email")
        print("3. Phone")
        print("4. Back")
        searchChoice = input("Enter choice: ")

        match searchChoice:
            case '1':
                newName = input("Enter updated name: ")
                contact.name = newName

            case '2':
                newEmail = input("Enter updated email: ")
                contact.email = newEmail
            case '3':
                newPhone = input("Enter updated phone: ")
                contact.phoneNumber = newPhone
            case '4':
                return
            case _:
                print("Invalid choice")

# --- Main Driver ---
fileName = "contacts.db"
fieldNames = ['ID', 'Name', 'Email', 'Phone']

initialize_database(fileName)


while True:
    print("Press 1 to add contact")
    print("Press 2 to search contact")
    print("Press 3 to delete contact")
    print("Press 4 to update contact")
    print("Press 5 to print all contacts")
    print("Press 6 to quit")
    choice = input("Enter choice: ")

    match choice:
        case '1':
            contact, next_id = get_contact(next_id)

            if not is_duplicate(contact, contacts):
                contacts.append(contact)
            else:
                print("Contact already exists.")

        case '2':

            search(contacts)


        case '3':
            searchedName = input("Enter ID number to delete: ").strip()

            for contact in contacts:
                if int(searchedName) == contact.contactID:
                    contacts.remove(contact)

        case '4':
            searchedID = input("Enter contact ID: ")

            for contact in contacts:
                if int(searchedID) == contact.contactID:
                    updateContact(contact)

        case '5':
            print("\nAll Contacts")
            print("------------")
            for contact in sorted(contacts, key=lambda c: c.name.lower()):
                print(contact)

        case '6':
            writeContacts(fileName, fieldNames, contacts)
            break

        case _:
            print("Invalid choice")



