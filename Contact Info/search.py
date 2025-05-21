def search_name(contacts, name_query):
    return [c for c in contacts if name_query.lower() in c.name.lower()]

def search_email(contacts,email_query):
    return [c for c in contacts if email_query.lower() in c.email.lower()]

def search_phone(contacts, phone_query):
    return [c for c in contacts if phone_query == c.phoneNumber]


def search_id(contacts, id_query):
    try:
        id_int = int(id_query)
        return [c for c in contacts if c.contactID == id_int]
    except ValueError:
        return []


def search(contacts):
    print("Search by:")
    print("1. Name")
    print("2. Email")
    print("3. Phone")
    print("4. ID")
    print("5. Back")
    search_choice = input("Enter choice: ")

    if search_choice == '1':
        query = input("Enter name to find: ").strip()
        results = search_name(contacts, query)
    elif search_choice == '2':
        query = input("Enter email to find: ").strip()
        results = search_email(contacts, query)
    elif search_choice == '3':
        query = input("Enter phone number to find: ").strip()
        results = search_phone(contacts, query)
    elif search_choice == '4':
        query = input("Enter contact ID to find: ").strip()
        results = search_id(contacts, query)
    elif search_choice == '5':
        return
    else:
        print("Invalid choice.")
        return

    if results:
        for contact in results:
            print(contact)
    else:
        print("Contact not found.")
