import sqlite3
import contact

def initialize_database(file_name='contacts.db'):
    with sqlite3.connect(file_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_contact(contact: Contact):
    with sqlite3.connect("contacts.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contacts (id, name, email, phone)
            VALUES (?, ?, ?, ?)
        """, (contact.contactID, contact.name, contact.email, contact.phoneNumber))
        conn.commit()


