"""Burger combo program use to store a quick menu of combo meals v3
develop the output_all function to display all the combos available in the program
Created by Qingxiao
"""
# pylint: disable = W0621, W0612, C0103

combos = {
         "Value": {
             "Combo name": "Value",
             "Combo items": [
                 {"Item": "Beef burger", "Price": 5.69},
                 {"Item": "Fries", "Price": 1.00},
                 {"Item": "Fizzy drink", "Price": 1.00}
             ]
         },
         "Cheezy": {
             "Combo name": "Cheezy",
             "Combo items": [
                 {"Item": "Cheeseburger", "Price": 6.69},
                 {"Item": "Fries", "Price": 1.00},
                 {"Item": "Fizzy drink", "Price": 1.00}
             ]
         },
         "Super": {
             "Combo name": "Super",
             "Combo items": [
                 {"Item": "Cheeseburger", "Price": 6.69},
                 {"Item": "Large fries", "Price": 2.00},
                 {"Item": "Smoothie", "Price": 2.00}
             ]
         }
     }


def add_combo():
    pass

def find_combo(combos, search_input):
    """Find combo meal based on user input"""
    found_combo = [
        combo for combo in combos.values() if combo["Combo name"].lower() == search_input.lower()
    ]#Find combo based on user input

    if found_combo:
        for combo in found_combo:
            print(f"Combo name: {combo['Combo name']}")
            for item in combo["Combo items"]:
                print(f"{item['Item']} - {item['Price']:.2f}")
            print()
    else:
        print("No combo meal found.")

def delete_combo():
    pass

def Output_all(combos):
    """Output all available combos"""
    if combos:
        message = "Here are all the available combos:\n\n"
        for combo_id, combo in combos.items():
            items_str = "\n".join([
                f"    {i+1}. {item['Item']} (${item['Price']:.2f})"
                for i, item in enumerate(combo['Combo items'])
            ])  # Create a string of items
            total_price = sum(item["Price"] for item in combo["Combo items"])# Calculate total price
            message += (
                f"Combo ID: {combo_id}\n"
                f"Name: {combo['Combo name']}\n"
                f"Total Price: ${total_price:.2f}\n"
                f"Includes:\n{items_str}\n"
                f"{'-' * 30}\n"
            )
        print(message)
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
        search_input = input(
            "\nEnter the name of the combo you want to find (e.g. Value, Cheezy, Super): "
        ).strip()
        find_combo(combos, search_input)

    elif choice == "3":
        delete_combo()

    elif choice == "4":
        Output_all(combos)

    elif choice == "5":
        print("Goodbye!")
    else:
        print("\nYou cannot leave this blank or enter an invalid choices. Please try again.")
