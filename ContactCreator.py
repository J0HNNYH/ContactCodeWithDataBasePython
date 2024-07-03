#imports sqlite for database
import sqlite3
#imports system functions for screen clearing
import os
#imports time so delays can happen
import time

#creates and database for the contacts
#connects that database to the program
conn = sqlite3.connect("contacts.db")
#creates an object named cursor that allows the program to manipulate the database
cursor = conn.cursor()
#creates table table named contacts with the values of id, name, phone_number, and email_address
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    email_address TEXT
)
""")
#applies changes made to the database
conn.commit()
    
#creates a function to clear screen
def clear():
    os.system('cls')
#creates function to create contact
def add_contact(name, phone_number, email_address):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
#creates a row in the table 'contacts' with the values inputed into the function
    cursor.execute("INSERT INTO contacts (name, phone_number, email_address) VALUES (?, ?, ?)", (name, phone_number, email_address))
#applies changes
    conn.commit()

#creates function to delete contacts
def delete_contact(name):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
#gets the name that was given to function and searches database
#when a value with the same name is found, that entire row is found
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name, ))
#applies changes
    conn.commit()
#creates function that searches database for a contact
def search_contacts(name):
    conn = sqlite3.connect("contacts.db")
    cursor  = conn.cursor()
#takes variable put into function and searches database for a value with the same name
#when a value is found the entire row is selected
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name, ))
#takes row that was selected and brings it into program
    contact = cursor.fetchone()
#return and prints the value of selected row
#if there is no value, 'contact not found' is printed instead
    return contact if contact else "Contact not found . . . "

#creates contact to display all contacts
def display_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
#selects every row from the table contacts
    cursor.execute("SELECT * FROM contacts")
#brings every selected row and value into program
    contact = cursor.fetchall()
#loops the printing once for every row that is selected
    for contact in contact:
#prints the info of contact with the name on a separate row
        print(f" * Name: {contact[1]}\n Phone {contact[2]}  Email: {contact[3]}")

def main():
#loops code for as long as the program is running
    while True:
#clears screen whenever the contact menu screen is displaying
        clear()
#displays all available options for user to input
        print("Contact Menu")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contacts")
        print("4. Display All Contacts")
        print("5. Quit")
#takes user's choice
        choice = input(">> ")
#checks if user's choice is number 1
        if choice == '1':
#clears screen when contact creator screen is displaying
            clear()
#displays lines for the user to input contact information
            fname = input("Enter name: ")
            fphone_number = input("Enter phone number: ")
            femail_address = input("Enter email: ")
#calls upon the add_contact function and gives it that values for the new contact
            add_contact(fname, fphone_number, femail_address)
#creates a blocker so the screen does not automatically clear and go back to contact menu screen
            blank = input("<<==ENTER")

#checks if user's choice is number 2
        elif choice == '2':
#clears screen when contact delete screen is displaying
            clear()
#displays line for user to specify which contact is being deleted
            fname = input("Enter name: ")
#calls upon the delete_contact function and gives the contact's name
            delete_contact(fname)
#creates animation to verify to the user that the contact is being deleted
            for i in range(2):
                clear()
                print("deleting ")
                time.sleep(1/2)
                clear()
                print("deleting .")
                time.sleep(1/2)
                clear()
                print("deleting . .")
                time.sleep(1/2)
                clear()
                print("deleting . . .")
                time.sleep(1/2)
#creates a blocker so the screen does not automatically clear and go back to contact menu screen
            blank = input("<<==ENTER")
#checks if user input is number 3
        elif choice == '3':
#clears screen when contact search screen is being displayed
            clear()
#creates line for user to specify which contact they want to see the information of
            name = input("Enter Contact: ")
#creates object named contact that calls upon the function search_contacts and gives it the value that the user has input
            contact = search_contacts(name)
#checks if the contact is a tuple (meaning that the values are not able to be changed)
            if isinstance(contact, tuple):
#displays the contact info of requested contact
                print(f" * Name: {contact[1]}\n * Phone {contact[2]}\n * Email: {contact[3]}")
            else:
#displays the contact info of requested contact
                print(contact)
#creates a blocker so the screen does not automatically clear and go back to contact menu screen
            blank = input("<<==ENTER")
        elif choice == '4':   
#clears screen when contact display screen is displaying
            clear()
#calls upon the display_contacts function
            display_contacts()
#creates a blocker so the screen does not automatically clear and go back to contact menu screen
            blank = input("<<==ENTER")
#checks if user's choice is number 5
        elif choice == '5':
#stops program
            break
#gives an output if the user input is not a number 1-5
        else:
#creates animation to show user that the value they have input is not valid
            for i in range(3):
                clear()
                print("Invalid choice . . . ")
                time.sleep(1/2)
                clear()
                time.sleep(1/2)

#calls upon the main function so it runs
main()
                  


