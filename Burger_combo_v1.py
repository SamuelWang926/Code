"""Burger combo program use to store a quick menu of combo meals v1
Set up variables
Created by Qingxiao
"""

# pylint: disable = W0621, W0612, C0103

def add_combo():
    pass

def find_combo():
    pass

def delete_combo():
    pass

def Output_all():
    pass

#main routine

roll = []

choice = ""
while choice != "5":
    print("What would you like to do?")
    print()
    print("1. Add a combo")
    print("2. Find a combo")
    print("3. Delete a combo")
    print("4. Output all combos")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_combo()

    elif choice == "2":
        find_combo()

    elif choice == "3":
        delete_combo()

    elif choice == "4":
        Output_all()

    elif choice == "5":
        print("Goodbye!")
    else:
        print("\nYou cannot leave this blank or enter invalid choices. Please try again.")
